from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field

# Health
class HealthResponse(BaseModel):
    status: str = "healthy"
    timestamp: str
    database: str = "connected"
    engine: str = "MySQL"

# Customer Balance
class BalanceResponse(BaseModel):
    customer_id: str
    total_earned: float
    pending: float
    available: float
    redeemed: float
    expired: float
    cancelled: float

# Earn Coupon
class EarnCouponRequest(BaseModel):
    customer_id: str
    customer_name: Optional[str] = "Customer"
    booking_ref: str
    office_id: Optional[str] = None
    booking_type: Optional[str] = None
    supplier: Optional[str] = None
    airline: Optional[str] = None
    fare_type: Optional[str] = None
    per_type: Optional[str] = "Net Fare"
    fare_limit: Optional[float] = None
    flat_amount: Optional[float] = None
    percent: Optional[float] = None
    coupon_percent: Optional[float] = None
    booking_fare: Optional[float] = Field(default=0.0, description="Total booking fare")
    travel_date: str
    booking_date: Optional[str] = None

class EarnCouponResponse(BaseModel):
    status: str = "success"
    txn_id: str
    coupon_earned: float
    coupon_percent: float
    coupon_status: str = "Pending"
    eligibility_date: str
    message: str = "Coupon will be available after travel completion"

# Release Coupon
class ReleaseCouponRequest(BaseModel):
    booking_ref: str

class ReleaseCouponResponse(BaseModel):
    status: str = "success"
    txn_id: str
    coupon_amount: float
    new_status: str = "Eligible"

# Redeem Coupon
class RedeemCouponRequest(BaseModel):
    customer_id: str
    booking_ref: str
    amount_to_redeem: float = Field(ge=0)
    booking_fare: float = Field(ge=0)

class RedeemCouponResponse(BaseModel):
    status: str = "success"
    redemption_id: str
    txn_id: str
    coupon_redeemed: float
    booking_fare: float
    customer_payable: float
    remaining_coupon_balance: float

# Reverse Coupon
class ReverseCouponRequest(BaseModel):
    original_booking_ref: str
    reason: str
    remarks: Optional[str] = None

class ReverseCouponResponse(BaseModel):
    status: str = "success"
    txn_id: str
    action: str = "Reversed"
    coupon_amount: float
    message: str = "Coupon reversed successfully"

# Ledger
class LedgerItem(BaseModel):
    txn_id: str
    customer_id: str
    booking_ref: str
    type: str
    txn_type: str
    booking_fare: float
    coupon_percent: float
    coupon_earned: float
    amount: float
    status: str
    date: str
    travel_date: Optional[str] = None

class LedgerResponse(BaseModel):
    customer_id: str
    ledger: List[LedgerItem]

# Customer Models
class CustomerCreate(BaseModel):
    id: Optional[str] = None
    customer_id: Optional[str] = None
    name: str
    email: str
    phone: Optional[str] = None
    status: Optional[str] = "Active"

class CustomerResponse(BaseModel):
    id: str
    customer_id: str
    name: str
    email: str
    phone: Optional[str] = None
    status: str
    created_at: Optional[str] = None

class ClientLoginRequest(BaseModel):
    customer_id: str
    email: str

class ClientLoginResponse(BaseModel):
    status: str
    message: str
    customer: CustomerResponse

# Booking Models
class BookingCreate(BaseModel):
    ref: Optional[str] = None
    booking_ref: Optional[str] = None
    customer: Optional[str] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    client: Optional[str] = None
    email: Optional[str] = None
    client_email: Optional[str] = None
    phone: Optional[str] = None
    mobile: Optional[str] = None
    client_mobile: Optional[str] = None
    supplier: Optional[str] = None
    airline: Optional[str] = None
    fare_type: Optional[str] = None
    fare: Optional[float] = None
    booking_fare: Optional[float] = None
    net_amount: Optional[float] = None
    travel: Optional[str] = None
    travel_date: Optional[str] = None
    booking_date: Optional[str] = None
    booked_date: Optional[str] = None
    airline_pnr: Optional[str] = None
    booking_type: Optional[str] = None
    sector: Optional[str] = None
    parent_pnr: Optional[str] = None
    pax_name: Optional[str] = None
    source_status: Optional[str] = None
    username: Optional[str] = None
    status: Optional[str] = "Confirmed"

class BookingResponse(BaseModel):
    ref: str
    booking_ref: str
    customer: str
    customer_id: str
    customer_name: Optional[str] = None
    client: Optional[str] = None
    supplier: Optional[str] = None
    airline: Optional[str] = None
    fare_type: Optional[str] = None
    fare: float
    booking_fare: float
    net_amount: Optional[float] = None
    travel: str
    travel_date: str
    booking_date: Optional[str] = None
    booked_date: Optional[str] = None
    status: str
    airline_pnr: Optional[str] = None
    booking_type: Optional[str] = None
    sector: Optional[str] = None
    parent_pnr: Optional[str] = None
    pax_name: Optional[str] = None
    source_status: Optional[str] = None
    username: Optional[str] = None

# Rule Models
class RuleCreate(BaseModel):
    rule_id: Optional[str] = None
    office_id: Optional[str] = None
    booking_type: Optional[str] = None
    supplier: Optional[str] = None
    airline: Optional[str] = None
    fare_type: Optional[str] = None
    percent: Optional[float] = None
    coupon_percent: Optional[float] = None
    priority: Optional[int] = 0
    status: Optional[str] = "Active"

class RuleResponse(BaseModel):
    id: Optional[int] = None
    rule_id: str
    office_id: Optional[str] = "-"
    booking_type: Optional[str] = "-"
    supplier: Optional[str] = "-"
    airline: Optional[str] = "-"
    fare: Optional[str] = "-"
    fare_type: Optional[str] = "-"
    percent: float
    coupon_percent: float
    priority: int
    status: str

# Settings Model
class SettingsSchema(BaseModel):
    min_redemption: float = 100.0
    max_redemption: float = 50000.0
    expiry_days: int = 365
    allow_partial_redemption: bool = True
    allow_combined_offers: bool = False


# Authentication Schemas
class AdminLoginRequest(BaseModel):
    email: str
    password: str

class AdminRegisterRequest(BaseModel):
    name: str
    email: str
    password: str

class AdminUserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: Optional[str] = None

class LoginResponse(BaseModel):
    status: str = "success"
    message: str = "Login successful"
    token: str
    expires_in_seconds: int = 300  # 5 minutes
    user: AdminUserResponse
