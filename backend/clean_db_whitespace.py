import database
from sqlalchemy import text

db = database.SessionLocal()
try:
    print("Deduplicating and merging customers...")
    db.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))

    # Delete untrimmed duplicate coupon_balance rows if trimmed exists
    db.execute(text("""
        DELETE b1 FROM coupon_balance b1
        INNER JOIN coupon_balance b2 
        ON TRIM(b1.customer_id) = b2.customer_id 
        AND b1.customer_id != b2.customer_id;
    """))

    # Update all references in bookings, coupons, ledger, balance to trimmed customer_id
    db.execute(text("UPDATE bookings SET customer_id = TRIM(customer_id) WHERE customer_id IS NOT NULL;"))
    db.execute(text("UPDATE coupons SET customer_id = TRIM(customer_id) WHERE customer_id IS NOT NULL;"))
    db.execute(text("UPDATE coupon_ledger SET customer_id = TRIM(customer_id) WHERE customer_id IS NOT NULL;"))
    db.execute(text("UPDATE coupon_balance SET customer_id = TRIM(customer_id) WHERE customer_id IS NOT NULL;"))

    # Delete untrimmed duplicate customer rows if trimmed version exists
    db.execute(text("""
        DELETE c1 FROM customers c1
        INNER JOIN customers c2 
        ON TRIM(c1.customer_id) = c2.customer_id 
        AND c1.customer_id != c2.customer_id;
    """))

    # Now trim remaining customers
    db.execute(text("UPDATE customers SET customer_id = TRIM(customer_id), email = TRIM(email);"))
    db.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
    db.commit()
    print("DATABASE CLEANED AND MERGED PERFECTLY!")

    res = db.execute(text("SELECT customer_id, name, email FROM customers WHERE customer_id = 'RCPNQ0500104';")).fetchall()
    print("FINAL ROW:", res)
except Exception as e:
    print("ERROR:", e)
    db.rollback()
finally:
    db.close()


