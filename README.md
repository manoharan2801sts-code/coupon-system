# ✈️ Coupon Management System

A full-stack coupon lifecycle and loyalty management web application built with **FastAPI**, **MySQL 8.0**, and **Vanilla HTML5/CSS3/JavaScript**.

---

## 📁 Project Directory Structure

```
files 1/
│
├── 📂 backend/                     # FastAPI Backend & MySQL Database Layer
│   ├── main.py                     # Main FastAPI server with all 13 REST APIs
│   ├── database.py                 # MySQL database connection & session pool
│   ├── models.py                   # SQLAlchemy ORM data models
│   ├── schemas.py                  # Pydantic v2 request/response validation
│   ├── schema.sql                  # MySQL 8.0 schema & seed data
│   ├── test_backend.py             # Automated API test suite
│   ├── requirements.txt            # Python dependencies
│   └── .env                        # MySQL connection credentials
│
├── 📂 frontend/                    # Frontend UI Application
│   ├── index.html                  # Main Web Application UI
│   └── frontend-complete.html      # Complete standalone UI
│
├── 📂 docs/                        # Complete Project Documentation
│   ├── QUICK_START.md              # 10-Minute quick setup guide
│   ├── FRONTEND_GUIDE.md           # Frontend architecture & integration guide
│   ├── UI_GUIDE.md                 # UI theme, design system & screenshots
│   ├── FILE_INDEX.md               # Master file navigation index
│   ├── FRONTEND_DELIVERY_SUMMARY.md# Deliverables summary
│   └── READ_ME_FIRST.txt           # Original overview
│
├── 🚀 start_all.bat                # 1-Click launcher (Backend + Frontend)
├── ⚙️ start_backend.bat            # 1-Click launcher (Backend only)
├── 🌐 start_frontend.bat           # 1-Click launcher (Frontend only)
└── 📄 README.md                    # Project README
```

---

## ⚡ Quick Start (Run the App)

### Option 1: 1-Click Launcher (Easiest)
Double-click **`start_all.bat`**.

---

### Option 2: Run via VS Code Terminal

#### 1️⃣ Start Backend:
```powershell
cd backend
python main.py
```
> 🌐 Backend URL: `http://localhost:8000`  
> 📖 Swagger API Docs: `http://localhost:8000/docs`

#### 2️⃣ Start Frontend:
Open a second terminal tab in VS Code and run:
```powershell
cd frontend
python -m http.server 5000
```
> 🎨 Frontend URL: `http://localhost:5000/index.html`

#### 3️⃣ Run Tests:
```powershell
cd backend
python test_backend.py
```

---

## 🗄️ Database Configuration

- **Database:** `coupon_db`
- **Host:** `localhost:3306`
- **User:** `root`
- Credentials can be changed anytime inside `backend/.env`.
