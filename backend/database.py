import os
import sys
import pymysql
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Load .env from current backend directory or parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Mano@2005")
DB_NAME = os.getenv("DB_NAME", "coupon_db")

# Step 1: Ensure the database exists in MySQL
def ensure_database_exists():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            charset="utf8mb4"
        )
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        conn.commit()
        conn.close()
        print(f"[OK] MySQL Database `{DB_NAME}` ensured.")
    except Exception as e:
        print(f"[WARNING] Database verification error: {e}")

ensure_database_exists()

# Step 2: Create SQLAlchemy Engine
from urllib.parse import quote_plus

raw_db_url = os.getenv("DATABASE_URL")
connect_args = {}

if raw_db_url:
    if raw_db_url.startswith("mysql://"):
        raw_db_url = raw_db_url.replace("mysql://", "mysql+pymysql://", 1)
    if "/sys" in raw_db_url:
        raw_db_url = raw_db_url.replace("/sys", "/coupon_db")
    DATABASE_URL = raw_db_url
    if "tidbcloud.com" in DATABASE_URL or "ssl" in DATABASE_URL.lower() or ":4000" in DATABASE_URL:
        connect_args = {"ssl": {"ssl_mode": "REQUIRED"}}
else:
    encoded_password = quote_plus(DB_PASSWORD)
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
    if DB_PORT == 4000 or "tidbcloud.com" in DB_HOST:
        connect_args = {"ssl": {"ssl_mode": "REQUIRED"}}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# FastAPI Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
