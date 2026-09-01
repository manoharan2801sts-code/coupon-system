# 🚀 Quick Start Guide - Complete System Setup

**Get the entire Coupon Management System running in 10 minutes!**

---

## 📦 What You Have

```
✅ Backend (FastAPI + PostgreSQL)
✅ Frontend (HTML + CSS + JavaScript)
✅ Database (Schema + Sample Data)
✅ Complete Documentation
```

---

## 🎯 Prerequisites

- **Python 3.9+** (for backend)
- **PostgreSQL 12+** (for database)
- **Modern Browser** (Chrome, Firefox, Safari, Edge)
- **Terminal/Command Line** access

---

## ⚡ 5-Minute Quick Start

### Step 1: Database Setup (2 minutes)

```bash
# Create database
createdb coupon_db

# Load schema (creates tables, indexes, sample data)
psql -U postgres -d coupon_db -f schema.sql

# Verify installation
psql -U postgres -d coupon_db -c "\dt"
# You should see 8 tables: customers, coupon_balance, coupon_ledger, etc.
```

**Troubleshooting**:
- If `createdb` not found: Add PostgreSQL to PATH or use full path
- If password required: `psql -U postgres` and enter password

### Step 2: Backend Setup (2 minutes)

```bash
# Install Python dependencies
pip install -r requirements.txt

# Start backend server
python coupon_backend_complete.py

# You should see:
# ✅ Starting Coupon Management System Backend
# ✅ Database connected
# ✅ Running on http://127.0.0.1:8000
```

**Verify backend is running**:
- Open browser: http://localhost:8000/docs
- Should see interactive API documentation

### Step 3: Frontend Setup (1 minute)

```bash
# Option A: Simple HTTP server
python -m http.server 5000

# Option B: Use another terminal and navigate to frontend file
# Then open in browser: http://localhost:5000/frontend-complete.html

# Option C: Direct file open
open frontend-complete.html
# (or double-click the file)
```

---

## ✅ Verification Checklist

Run these commands to verify everything works:

### 1. Check Database
```bash
psql -U postgres -d coupon_db -c "SELECT COUNT(*) FROM customers;"
# Should return: 3 (sample customers)
```

### 2. Check Backend API
```bash
# In another terminal
curl http://localhost:8000/api/health

# Should return:
# {"status": "healthy", "timestamp": "2024-11-28T..."}
```

### 3. Check Balance
```bash
curl http://localhost:8000/api/coupon/balance/CUST001

# Should return:
# {
#   "customer_id": "CUST001",
#   "total_earned": 5000,
#   "available": 4500,
#   ...
# }
```

### 4. Open Frontend
- Navigate to: http://localhost:5000/frontend-complete.html
- You should see the dashboard with metrics loaded

---

## 🎨 What You Can Do Now

### Test Coupon Earning
1. Go to **Coupons** page
2. Fill in "Earn Coupon" form:
   - Customer ID: `CUST001`
   - Booking Reference: `BK-TEST-001`
   - Booking Fare: `10000`
   - Travel Date: Tomorrow's date
3. Click "Earn Coupon"
4. See confirmation: ✅ Coupon earned ₹300

### Check Customer Balance
1. Go to **Coupons** page
2. Click "Check Balance" button
3. Enter: `CUST001`
4. See all balance details

### View Transaction History
1. Go to **Ledger** page
2. See all transactions for CUST001
3. Search by Customer ID using filter

### Manage Rules
1. Go to **Rules** page
2. Click "Add Rule"
3. Set coupon percentage (e.g., 2.5%)
4. Save rule
5. See active rules displayed

### Redeem Coupons
1. Go to **Coupons** page
2. Click "Redeem Coupon"
3. Enter customer ID and booking details
4. Drag slider to select redemption amount
5. See real-time calculation of customer payment
6. Click "Redeem Coupon"

---

## 📊 Sample Data Included

### Pre-loaded Customers
```
CUST001 - Rajesh Kumar (rajesh@email.com)
CUST002 - Priya Sharma (priya@email.com)
CUST003 - Amit Patel (amit@email.com)
```

### Pre-loaded Rules
```
Supplier A + IndiGo + Super 6E = 3% (Priority 7)
Supplier A + IndiGo = 2% (Priority 6)
Supplier A = 1.5% (Priority 5)
IndiGo = 1.5% (Priority 4)
Global = 1% (Priority 0)
```

### Pre-loaded Bookings
```
BK-2024-001: Delhi → Mumbai, IndiGo, ₹8,500
BK-2024-002: Mumbai → Bangalore, Air India, ₹9,200
```

---

## 🧪 Full Test Flow

Follow this complete workflow to test all features:

### 1. Dashboard
- [x] See metrics loaded
- [x] See recent transactions
- [x] See system status

### 2. Customers
- [x] View customer list
- [x] View customer balance
- [x] Add new customer

### 3. Earn Coupon
- [x] Earn coupon for CUST001
- [x] See status: Pending
- [x] Check updated balance

### 4. Release Coupon
- [x] Release pending coupon
- [x] See status: Eligible
- [x] Coupon available for redemption

### 5. Redeem Coupon
- [x] Redeem ₹5,000 from available balance
- [x] See real-time calculation
- [x] Confirm customer payable amount

### 6. View Ledger
- [x] See all transactions
- [x] See transaction types
- [x] Filter by customer ID

### 7. Manage Rules
- [x] Add new rule with 2% coupon
- [x] See rule displayed
- [x] Verify rule priority

### 8. Configure Settings
- [x] View global settings
- [x] Update min/max redemption
- [x] Save settings

---

## 🌐 Multi-Terminal Setup

If you prefer running everything in separate terminals:

**Terminal 1 - PostgreSQL** (if not running as service):
```bash
postgres -D /path/to/postgres/data
```

**Terminal 2 - Backend**:
```bash
python coupon_backend_complete.py
# Watch for: "Application startup complete"
```

**Terminal 3 - Frontend Server**:
```bash
python -m http.server 5000
# Watch for: "Serving HTTP on 0.0.0.0 port 5000"
```

**Terminal 4 - Browser**:
```bash
# Open browser to:
# http://localhost:5000/frontend-complete.html
```

---

## 🔧 Configuration

### Change Backend Port
**If port 8000 is busy:**

1. Start backend on different port:
   ```bash
   python coupon_backend_complete.py --port 9000
   ```

2. Update frontend API URL:
   ```javascript
   // In frontend-complete.html, find:
   const app = {
       apiBase: 'http://localhost:9000/api'  // Change this
   };
   ```

### Change Frontend Port
**If port 5000 is busy:**

```bash
python -m http.server 8080
# Then open: http://localhost:8080/frontend-complete.html
```

### Use Different Database
**If you have existing PostgreSQL:**

```bash
# Update connection in backend
export DATABASE_URL="postgresql://user:password@localhost:5432/coupon_db"

# Then start backend
python coupon_backend_complete.py
```

---

## 🐛 Troubleshooting

### Problem: "Address already in use"

```bash
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>

# Or use different port
python coupon_backend_complete.py --port 9000
```

### Problem: Database connection error

```bash
# Check PostgreSQL is running
psql -U postgres -c "SELECT 1;"

# If not running, start it:
# macOS: brew services start postgresql
# Linux: sudo service postgresql start
# Windows: net start postgresql-x64-13
```

### Problem: "No module named 'fastapi'"

```bash
# Install dependencies
pip install -r requirements.txt

# Or install individually
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

### Problem: Frontend not loading

```bash
# Check backend is running
curl http://localhost:8000/api/health

# Check frontend port
# Open: http://localhost:5000/frontend-complete.html

# Check browser console for errors
# Press F12 → Console tab
```

### Problem: API calls failing

```bash
# Check CORS is enabled
# Add to backend if needed:
# See FRONTEND_GUIDE.md → CORS Configuration

# Check API base URL matches
# In frontend, should be: http://localhost:8000/api
```

---

## 📈 Next Steps After Setup

### 1. Explore the Features
- Try each page and form
- Test error handling
- Experiment with filters

### 2. Review Code
- Read comments in `frontend-complete.html`
- Study API calls in JavaScript
- Review backend in `coupon_backend_complete.py`

### 3. Customize
- Change company name/branding
- Add custom pages
- Modify calculations

### 4. Integrate with Real Systems
- Connect to actual booking platform API
- Add email notifications
- Setup webhooks

### 5. Deploy
- Follow FRONTEND_GUIDE.md → Deployment
- Setup production database
- Configure HTTPS/SSL

---

## 📚 Documentation Map

| Document | Purpose | Read When |
|----------|---------|-----------|
| **QUICK_START.md** | Setup & run (this file) | First time setup |
| **FRONTEND_GUIDE.md** | Frontend detailed guide | Customizing UI |
| **README.md** | Backend API docs | Integrating APIs |
| **DEPLOYMENT_GUIDE.md** | Production setup | Deploying to production |
| **PROJECT_SUMMARY.md** | Overview of entire system | Understanding architecture |

---

## ✨ Key Features to Explore

### 1. Real-time Calculation
- Go to Coupons → Redeem Coupon
- Drag slider
- See instant update of customer payment amount

### 2. Live Filtering
- Go to Ledger page
- Type in customer filter
- Table filters in real-time

### 3. Smart Alerts
- All forms show success/error alerts
- Auto-dismiss after 4 seconds
- Color-coded by type

### 4. Responsive Design
- Resize browser window
- Open on mobile device
- See layout adapt perfectly

### 5. API Integration
- Open browser DevTools (F12)
- Go to Network tab
- Perform an action
- See API call details

---

## 🎓 Learning Paths

### Path 1: User (5 minutes)
1. Open frontend
2. Explore each page
3. Try earning/redeeming coupons

### Path 2: Developer (30 minutes)
1. Read this quick start
2. Read FRONTEND_GUIDE.md
3. Read README.md
4. Review code in files

### Path 3: Administrator (15 minutes)
1. Setup everything
2. Load sample data
3. Configure rules
4. Test workflows

### Path 4: DevOps (20 minutes)
1. Setup local environment
2. Read DEPLOYMENT_GUIDE.md
3. Explore Docker options
4. Plan production setup

---

## 💡 Pro Tips

### Tip 1: Use Sample Data
- Pre-loaded customers: CUST001, CUST002, CUST003
- All operations will work with sample data
- No need to create customers first

### Tip 2: Monitor API Calls
```javascript
// Add to JavaScript console
fetch('http://localhost:8000/api/health')
    .then(r => r.json())
    .then(data => console.log('Backend OK:', data))
    .catch(e => console.error('Backend Error:', e))
```

### Tip 3: Check Database Directly
```bash
# View customers
psql -U postgres -d coupon_db -c "SELECT * FROM customers;"

# View rules
psql -U postgres -d coupon_db -c "SELECT * FROM coupon_rules;"

# View ledger
psql -U postgres -d coupon_db -c "SELECT * FROM coupon_ledger LIMIT 10;"
```

### Tip 4: Reset Database
```bash
# Drop and recreate
dropdb coupon_db
createdb coupon_db
psql -U postgres -d coupon_db -f schema.sql
```

---

## 🎯 Success Checklist

- [ ] PostgreSQL installed and running
- [ ] `createdb coupon_db` works
- [ ] `schema.sql` loaded successfully
- [ ] `pip install -r requirements.txt` completes
- [ ] Backend starts without errors
- [ ] `http://localhost:8000/docs` shows API docs
- [ ] Frontend HTML file opens in browser
- [ ] Dashboard loads with metrics
- [ ] Can earn a coupon
- [ ] Can view customer balance
- [ ] Can redeem a coupon
- [ ] Can view transaction ledger

**If all checked ✓ → System is ready!**

---

## 📞 Getting Help

### Check Logs
```bash
# Backend console output
# Look for errors when operations fail

# Frontend browser console
# Press F12 → Console tab → See error messages
```

### Check Files
- **Error in form?** → Check frontend HTML
- **Error in API?** → Check backend logs
- **Database error?** → Check PostgreSQL console

### Review Documentation
1. FRONTEND_GUIDE.md - Frontend issues
2. README.md - Backend/API issues
3. DEPLOYMENT_GUIDE.md - Setup issues

---

## 🎉 You're Ready!

**You now have a fully functional Coupon Management System!**

Enjoy exploring and customizing. If you need help, refer to:
- Inline code comments
- Complete documentation files
- Example workflows above

Happy coding! 🚀

---

**Version**: 1.0  
**Last Updated**: November 2024  
**Estimated Setup Time**: 10 minutes  
**Difficulty**: ⭐ Easy
