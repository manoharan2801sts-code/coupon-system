from datetime import datetime
from sqlalchemy import (
    Column,
    String,
    Numeric,
    Integer,
    DateTime,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(String(50), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    phone = Column(String(30), nullable=True)
    status = Column(String(20), nullable=False, default="Active")
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    balance = relationship("CouponBalance", back_populates="customer", uselist=False, cascade="all, delete-orphan")
    bookings = relationship("Booking", back_populates="customer", cascade="all, delete-orphan")
    coupons = relationship("Coupon", back_populates="customer", cascade="all, delete-orphan")
    redemptions = relationship("CouponRedemption", back_populates="customer", cascade="all, delete-orphan")
    ledger_entries = relationship("CouponLedger", back_populates="customer", cascade="all, delete-orphan")


class CouponBalance(Base):
    __tablename__ = "coupon_balance"

    customer_id = Column(String(50), ForeignKey("customers.customer_id", ondelete="CASCADE"), primary_key=True)
    total_earned = Column(Numeric(12, 2), nullable=False, default=0.00)
    pending = Column(Numeric(12, 2), nullable=False, default=0.00)
    available = Column(Numeric(12, 2), nullable=False, default=0.00)
    redeemed = Column(Numeric(12, 2), nullable=False, default=0.00)
    expired = Column(Numeric(12, 2), nullable=False, default=0.00)
    cancelled = Column(Numeric(12, 2), nullable=False, default=0.00)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    customer = relationship("Customer", back_populates="balance")


class CouponRule(Base):
    __tablename__ = "coupon_rules"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rule_id = Column(String(50), unique=True, nullable=False, index=True)
    office_id = Column(String(50), nullable=True)
    booking_type = Column(String(50), nullable=True)
    supplier = Column(String(100), nullable=True)
    airline = Column(String(100), nullable=True)
    fare_type = Column(String(100), nullable=True)
    coupon_percent = Column(Numeric(5, 2), nullable=False, default=1.00)
    priority = Column(Integer, nullable=False, default=0)
    status = Column(String(20), nullable=False, default="Active")
    created_at = Column(DateTime, default=datetime.utcnow)


class Booking(Base):
    __tablename__ = "bookings"

    booking_ref = Column(String(50), primary_key=True, index=True)
    customer_id = Column(String(50), ForeignKey("customers.customer_id", ondelete="CASCADE"), nullable=False, index=True)
    supplier = Column(String(100), nullable=True)
    airline = Column(String(100), nullable=True)
    fare_type = Column(String(100), nullable=True)
    booking_fare = Column(Numeric(12, 2), nullable=False, default=0.00)
    booking_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    travel_date = Column(DateTime, nullable=False)
    status = Column(String(30), nullable=False, default="Completed")
    created_at = Column(DateTime, default=datetime.utcnow)

    # --- Roundtrip / PNR-wise sales format fields (added for Roundtrip_COUPON.xlsx) ---
    airline_pnr = Column(String(50), nullable=True)
    booking_type = Column(String(50), nullable=True)      # e.g. Round Trip / One Way
    sector = Column(String(150), nullable=True)            # route, e.g. DEL-BOM-DEL
    parent_pnr = Column(String(50), nullable=True, index=True)  # links split/child PNRs to the original
    pax_name = Column(String(150), nullable=True)           # passenger name (customer_name may be the agency/client)
    source_status = Column(String(50), nullable=True)       # original "Status" column from the source export
    username = Column(String(100), nullable=True)           # booking agent username from source export

    customer = relationship("Customer", back_populates="bookings")


class Coupon(Base):
    __tablename__ = "coupons"

    coupon_id = Column(String(50), primary_key=True, index=True)
    booking_ref = Column(String(50), unique=True, nullable=False, index=True)
    customer_id = Column(String(50), ForeignKey("customers.customer_id", ondelete="CASCADE"), nullable=False, index=True)
    coupon_percent = Column(Numeric(5, 2), nullable=False, default=0.00)
    coupon_amount = Column(Numeric(12, 2), nullable=False, default=0.00)
    status = Column(String(30), nullable=False, default="Pending", index=True)
    eligibility_date = Column(DateTime, nullable=False)
    expiry_date = Column(DateTime, nullable=True)
    remarks = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    customer = relationship("Customer", back_populates="coupons")


class CouponRedemption(Base):
    __tablename__ = "coupon_redemptions"

    redemption_id = Column(String(50), primary_key=True, index=True)
    txn_id = Column(String(50), unique=True, nullable=False, index=True)
    customer_id = Column(String(50), ForeignKey("customers.customer_id", ondelete="CASCADE"), nullable=False, index=True)
    booking_ref = Column(String(50), nullable=False, index=True)
    amount_redeemed = Column(Numeric(12, 2), nullable=False, default=0.00)
    booking_fare = Column(Numeric(12, 2), nullable=False, default=0.00)
    customer_payable = Column(Numeric(12, 2), nullable=False, default=0.00)
    status = Column(String(30), nullable=False, default="Success")
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="redemptions")


class CouponLedger(Base):
    __tablename__ = "coupon_ledger"

    id = Column(Integer, primary_key=True, autoincrement=True)
    txn_id = Column(String(50), unique=True, nullable=False, index=True)
    customer_id = Column(String(50), ForeignKey("customers.customer_id", ondelete="CASCADE"), nullable=False, index=True)
    booking_ref = Column(String(50), nullable=False, index=True)
    txn_type = Column(String(50), nullable=False)
    booking_fare = Column(Numeric(12, 2), nullable=False, default=0.00)
    coupon_percent = Column(Numeric(5, 2), nullable=False, default=0.00)
    coupon_earned = Column(Numeric(12, 2), nullable=False, default=0.00)
    amount = Column(Numeric(12, 2), nullable=False, default=0.00)
    status = Column(String(30), nullable=False, default="Pending")
    travel_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    customer = relationship("Customer", back_populates="ledger_entries")


class SystemSetting(Base):
    __tablename__ = "system_settings"

    config_key = Column(String(50), primary_key=True)
    config_value = Column(String(255), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class AdminUser(Base):
    __tablename__ = "admin_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
