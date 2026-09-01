# 🎨 Frontend UI Guide - Complete Visual Walkthrough

**Visual guide to all pages, components, and features in the frontend**

---

## 🏗️ Application Layout

```
┌─────────────────────────────────────────────────────────────────┐
│                          TOPBAR                                  │
│  📊 Dashboard          [👤 Admin] [LOGOUT]                      │
└─────────────────────────────────────────────────────────────────┘
┌──────────────┬─────────────────────────────────────────────────┐
│              │                                                  │
│   SIDEBAR    │              MAIN CONTENT AREA                  │
│              │                                                  │
│ • Dashboard  │  ┌──────────────────────────────────────────┐  │
│ • Customers  │  │                                          │  │
│ • Coupons    │  │     Page Content                         │  │
│ • Bookings   │  │                                          │  │
│ • Redemptions│  │                                          │  │
│ • Ledger     │  │                                          │  │
│ • Rules      │  │                                          │  │
│ • Settings   │  │                                          │  │
│              │  │                                          │  │
│              │  └──────────────────────────────────────────┘  │
└──────────────┴─────────────────────────────────────────────────┘
```

---

## 📄 Page 1: Dashboard

### What You See
```
📊 Dashboard

Metrics (4 Cards):
┌──────────────┬──────────────┬──────────────┬──────────────┐
│ Available    │ Pending      │ Total Earned │ Expired      │
│ ₹4,500       │ ₹500         │ ₹5,000       │ ₹0           │
│ (Green)      │ (Orange)     │ (Blue)       │ (Red)        │
└──────────────┴──────────────┴──────────────┴──────────────┘

Recent Transactions (Left):              System Status (Right):
┌─────────────────────────┐             ┌──────────────────────┐
│ Coupon Earned           │             │ Backend Status       │
│ 2024-11-28              │             │ ✓ ONLINE             │
│ Amount: ₹300            │             │                      │
│ [Pending]               │             │ Database Connection  │
│                         │             │ ✓ CONNECTED          │
│ Coupon Released         │             │                      │
│ 2024-11-27              │             │ API Response         │
│ Amount: ₹300            │             │ ✓ 200 OK             │
│ [Eligible]              │             │                      │
└─────────────────────────┘             └──────────────────────┘
```

### Key Features
- ✅ Real-time metrics from backend API
- ✅ Color-coded status indicators
- ✅ Recent transactions feed
- ✅ System health monitoring
- ✅ Auto-updates on page visit

---

## 👥 Page 2: Customers

### What You See
```
👥 Customers

[+ ADD CUSTOMER]

┌────────────┬──────────────┬──────────────────────┬──────────────┐
│ Customer ID│ Name         │ Email                │ Phone        │
├────────────┼──────────────┼──────────────────────┼──────────────┤
│ CUST001    │ Rajesh Kumar │ rajesh@email.com    │ +91 9876...  │
│            │              │                      │ [View Balance]│
├────────────┼──────────────┼──────────────────────┼──────────────┤
│ CUST002    │ Priya Sharma │ priya@email.com     │ +91 9876...  │
│            │              │                      │ [View Balance]│
├────────────┼──────────────┼──────────────────────┼──────────────┤
│ CUST003    │ Amit Patel   │ amit@email.com      │ +91 9876...  │
│            │              │                      │ [View Balance]│
└────────────┴──────────────┴──────────────────────┴──────────────┘
```

### Add Customer Modal
```
┌─────────────────────────────────────────────┐
│ Add New Customer                        [×] │
├─────────────────────────────────────────────┤
│                                             │
│ Customer ID *                               │
│ [_________________ CUST004]                │
│                                             │
│ Name *                                      │
│ [_________________ John Doe]               │
│                                             │
│ Email *                                     │
│ [_________________ john@email.com]         │
│                                             │
│ Phone                                       │
│ [_________________ +91 9876...]            │
│                                             │
│              [Cancel] [Add Customer]       │
└─────────────────────────────────────────────┘
```

### Key Features
- ✅ View all customers
- ✅ Add new customer
- ✅ Quick balance lookup
- ✅ Contact information
- ✅ Status indicators

---

## 🎁 Page 3: Coupons

### Left Panel: Earn Coupon
```
┌──────────────────────────────┐
│ Earn Coupon                  │
├──────────────────────────────┤
│ Customer ID *                │
│ [CUST001______________]      │
│                              │
│ Booking Reference *          │
│ [BK-2024-001__________]      │
│                              │
│ Booking Fare *               │
│ [10000_______________]       │
│                              │
│ Supplier                     │
│ [Supplier A____________]     │
│                              │
│ Airline                      │
│ [IndiGo_____________]        │
│                              │
│ Fare Type                    │
│ [Super 6E___________]        │
│                              │
│ Travel Date *                │
│ [2024-12-10_____14:30]       │
│                              │
│ [Earn Coupon]                │
└──────────────────────────────┘
```

### Center Panel: Release Coupon
```
┌──────────────────────────────┐
│ Release Coupon               │
├──────────────────────────────┤
│ Booking Reference *          │
│ [BK-2024-001__________]      │
│                              │
│ [Release Coupon]             │
└──────────────────────────────┘
```

### Right Panel: Quick Actions
```
┌──────────────────────────────┐
│ Quick Actions                │
├──────────────────────────────┤
│ [Check Balance]              │
│                              │
│ [Redeem Coupon]              │
│                              │
│ [Reverse Coupon]             │
└──────────────────────────────┘
```

### Check Balance Modal
```
┌─────────────────────────────────────────────┐
│ Check Customer Balance              [×]     │
├─────────────────────────────────────────────┤
│ Customer ID                                 │
│ [CUST001____________]                      │
│                                             │
│ ┌────────────────────────────────────────┐ │
│ │ Available                 ₹4,500        │ │
│ │ Pending                   ₹500          │ │
│ │ Total Earned              ₹5,000        │ │
│ │ Redeemed                  ₹1,000        │ │
│ │ Expired                   ₹0            │ │
│ └────────────────────────────────────────┘ │
│                                             │
│         [Close] [Check Balance]             │
└─────────────────────────────────────────────┘
```

### Redeem Coupon Modal (★ Key Feature)
```
┌─────────────────────────────────────────────┐
│ Redeem Coupon                       [×]     │
├─────────────────────────────────────────────┤
│ Customer ID                                 │
│ [CUST001_________]                         │
│                                             │
│ Booking Reference                           │
│ [BK-2024-002_____]                         │
│                                             │
│ Booking Fare (₹)                            │
│ [12000__________]                          │
│                                             │
│ Amount to Redeem (₹)                        │
│ ₹0      ────●────────────    Max: ₹5,000   │
│             ₹5,000 (Display)                │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ Booking Fare        ₹12,000         │   │
│ │ Coupon Used         -₹5,000          │   │
│ │ ──────────────────────────           │   │
│ │ Customer Pays       ₹7,000           │   │
│ └──────────────────────────────────────┘   │
│                                             │
│      [Cancel] [Redeem Coupon]              │
└─────────────────────────────────────────────┘
```

### Real-time Calculation Display
```
Live Update as slider moves:
Slider at 0     → Customer Pays: ₹12,000
Slider at 2500  → Customer Pays: ₹9,500
Slider at 5000  → Customer Pays: ₹7,000
Slider at 7500  → Invalid (more than available)
```

### Key Features
- ✅ Earn coupon with rule matching
- ✅ Release coupon after travel
- ✅ Real-time redemption calculator
- ✅ Live payment calculation
- ✅ Reverse coupon functionality
- ✅ Three-step workflow support

---

## 📅 Page 4: Bookings

### What You See
```
📅 Bookings

[+ ADD BOOKING]

┌──────────┬──────────┬──────────┬─────────┬──────────┬────────┐
│ Booking  │ Customer │ Airline  │ Fare    │ Travel   │ Status │
│ Ref      │ ID       │          │         │ Date     │        │
├──────────┼──────────┼──────────┼─────────┼──────────┼────────┤
│ BK-2024- │ CUST001  │ IndiGo   │ ₹8,500  │ 2024-12- │ ✓      │
│ 001      │          │          │         │ 10       │ OK     │
├──────────┼──────────┼──────────┼─────────┼──────────┼────────┤
│ BK-2024- │ CUST001  │ Air India│ ₹9,200  │ 2024-12- │ ✓      │
│ 002      │          │          │         │ 20       │ OK     │
├──────────┼──────────┼──────────┼─────────┼──────────┼────────┤
│ BK-2024- │ CUST002  │ SpiceJet │ ₹7,500  │ 2024-12- │ ✓      │
│ 003      │          │          │         │ 15       │ OK     │
└──────────┴──────────┴──────────┴─────────┴──────────┴────────┘
```

### Add Booking Modal
```
┌────────────────────────────────────────────┐
│ Add New Booking                     [×]    │
├────────────────────────────────────────────┤
│ Booking Reference *                        │
│ [BK-2024-004________________]              │
│                                            │
│ Customer ID *                              │
│ [CUST001_____________]                    │
│                                            │
│ ┌─────────────────┬──────────────────┐    │
│ │ Supplier        │ Airline          │    │
│ │ [Supplier A]    │ [IndiGo]         │    │
│ └─────────────────┴──────────────────┘    │
│                                            │
│ Booking Fare *                             │
│ [10000________________]                   │
│                                            │
│ Travel Date *                              │
│ [2024-12-10________14:30]                 │
│                                            │
│        [Cancel] [Add Booking]             │
└────────────────────────────────────────────┘
```

### Key Features
- ✅ View all bookings
- ✅ Add new booking
- ✅ Track booking details
- ✅ Link to customers
- ✅ Travel date tracking

---

## 💳 Page 5: Redemptions

### What You See
```
💳 Redemption History

┌───────────┬──────────┬───────────┬─────────────┬─────────┬────────┐
│Redemption │ Customer │ Booking   │ Amount      │ Status  │ Date   │
│ID         │ ID       │ Ref       │ Redeemed    │         │        │
├───────────┼──────────┼───────────┼─────────────┼─────────┼────────┤
│ RED-001   │ CUST001  │ BK-2024-  │ ₹5,000      │ ✓ Success│ 2024- │
│           │          │ 002       │             │         │11-28  │
├───────────┼──────────┼───────────┼─────────────┼─────────┼────────┤
│ RED-002   │ CUST002  │ BK-2024-  │ ₹3,000      │ ✓ Success│ 2024- │
│           │          │ 003       │             │         │11-27  │
└───────────┴──────────┴───────────┴─────────────┴─────────┴────────┘
```

### Key Features
- ✅ Complete redemption history
- ✅ Amount and status tracking
- ✅ Customer linking
- ✅ Timestamp recording
- ✅ Status indicators

---

## 📋 Page 6: Ledger (★ Most Detailed)

### What You See
```
📋 Transaction Ledger

Filter: [CUST001__________]

┌─────────┬──────────┬───────┬────────────┬──────────┬─────────────┐
│Txn ID   │ Booking  │ Type  │ Amount     │ Status   │ Date        │
│         │ Ref      │       │            │          │             │
├─────────┼──────────┼───────┼────────────┼──────────┼─────────────┤
│ TXN-1   │ BK-2024- │Coupon │ +₹300      │ Pending  │2024-11-28   │
│         │001       │Earned │ (GREEN)    │          │10:00 AM     │
├─────────┼──────────┼───────┼────────────┼──────────┼─────────────┤
│ TXN-2   │ BK-2024- │Coupon │ +₹300      │ Eligible │2024-11-28   │
│         │001       │Release│ (GREEN)    │          │02:00 PM     │
├─────────┼──────────┼───────┼────────────┼──────────┼─────────────┤
│ TXN-3   │ BK-2024- │Coupon │ -₹5,000    │Redeemed │2024-11-28   │
│         │002       │Redeem │ (RED)      │          │03:30 PM     │
└─────────┴──────────┴───────┴────────────┴──────────┴─────────────┘

Real-time Filter:
Type "CUST002" → Table updates instantly to show only CUST002 transactions
```

### Key Features
- ✅ Complete transaction ledger
- ✅ All 20 ledger fields visible (on expand)
- ✅ Real-time search/filter
- ✅ Color-coded amounts (+ green, - red)
- ✅ Status badges
- ✅ Transaction type tracking

---

## ⚙️ Page 7: Rules (Priority Matching)

### What You See
```
⚙️ Rules Configuration

Left Panel: Add Rule
┌────────────────────────┐
│ Add Coupon Rule        │
├────────────────────────┤
│ Supplier (Opt.)        │
│ [Supplier A____]       │
│                        │
│ Airline (Opt.)         │
│ [IndiGo_______]        │
│                        │
│ Fare Type (Opt.)       │
│ [Flexi________]        │
│                        │
│ Coupon % *             │
│ [2.5_________]         │
│                        │
│ Priority               │
│ [7___________]         │
│                        │
│ Status                 │
│ [Active ▼]             │
│                        │
│ [Add Rule]             │
└────────────────────────┘

Right Panel: Active Rules
┌────────────────────────┐
│ Active Rules           │
├────────────────────────┤
│ Supplier A             │ 3%
│ IndiGo • Super 6E      │ ✓
│ Priority: 7            │ Active
│                        │
│ Supplier A             │ 2%
│ IndiGo                 │ ✓
│ Priority: 6            │ Active
│                        │
│ Global                 │ 1%
│ (No filters)           │ ✓
│ Priority: 0            │ Active
└────────────────────────┘
```

### Priority Hierarchy Display
```
Priority Levels (Highest to Lowest):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Level 1: Supplier + Airline + Fare Type  (Highest Specificity)
Level 2: Supplier + Airline
Level 3: Supplier
Level 4: Airline + Fare Type
Level 5: Airline
Level 6: Fare Type
Level 7: Global (No Filters)            (Lowest Specificity)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Example:
Booking: Supplier A + IndiGo + Super 6E
→ Matches Level 1: Uses 3% (highest priority wins)
```

### Key Features
- ✅ Add new rules
- ✅ Set coupon percentage
- ✅ Priority management
- ✅ Supplier/Airline/Fare Type matching
- ✅ Active/Inactive toggle
- ✅ Real-time display

---

## 🔧 Page 8: Settings

### What You See
```
🔧 Global Configuration

┌─────────────────────────────────────────┐
│ Global Configuration                    │
├─────────────────────────────────────────┤
│ ┌────────────────┬────────────────────┐ │
│ │ Min Redemption │ Max Redemption     │ │
│ │ [100]          │ [50000]            │ │
│ └────────────────┴────────────────────┘ │
│                                         │
│ ┌────────────────┬────────────────────┐ │
│ │ Coupon Expiry  │ Partial Redemption │ │
│ │ [365] Days     │ [Yes ▼]            │ │
│ └────────────────┴────────────────────┘ │
│                                         │
│ ┌────────────────┐                      │
│ │ Combined Offers│                      │
│ │ [No ▼]         │                      │
│ └────────────────┘                      │
│                                         │
│ [Save Settings]                         │
└─────────────────────────────────────────┘
```

### Key Features
- ✅ Min/Max redemption amounts
- ✅ Coupon expiry configuration
- ✅ Partial redemption toggle
- ✅ Combined offers configuration
- ✅ Save/persist settings

---

## 🎨 Color Scheme & UI Elements

### Color Palette
```
Primary Blue:      #1e3a8a (Dark Blue)
Primary Light:     #3b82f6 (Light Blue)
Secondary Green:   #059669 (Green)
Danger Red:        #dc2626 (Red)
Warning Orange:    #f59e0b (Orange)
Info Cyan:         #0ea5e9 (Cyan)
```

### Badge Types
```
✓ Success:  [GREEN BG]    Success / Active / Eligible
⏳ Pending:  [ORANGE BG]   Pending / Waiting
✗ Danger:  [RED BG]      Error / Expired / Failed
ℹ Info:    [BLUE BG]     Information
```

### Buttons
```
Primary Button:    [BLUE BG] WHITE TEXT    - Main actions
Secondary Button:  [GREEN BG] WHITE TEXT   - Confirm/Approve
Danger Button:     [RED BG] WHITE TEXT     - Delete/Reverse
Ghost Button:      [WHITE BG] BORDER       - Cancel/Secondary
Small Button:      Compact version of above
Disabled Button:   [FADED] CURSOR:NOT-ALLOWED
```

### Alert Types
```
✅ Success Alert   [GREEN BORDER LEFT] "✅ Operation successful"
❌ Error Alert     [RED BORDER LEFT]   "❌ Something went wrong"
⚠️ Warning Alert   [ORANGE BORDER]     "⚠️ Warning message"
ℹ️ Info Alert      [BLUE BORDER]       "ℹ️ Information"
```

---

## 📱 Responsive Behavior

### Desktop (1200px+)
```
┌──────────────────────────────────────────┐
│ [Sidebar: 280px] [Content: Full Width]   │
└──────────────────────────────────────────┘
Grid layouts: 3-4 columns
Table display: Full width
Modal: Max 600px width
```

### Tablet (768px - 1200px)
```
┌──────────────────────────────┐
│ [Sidebar Hidden] [Content]   │
└──────────────────────────────┘
Grid layouts: 2 columns
Table display: Scrollable
Modal: Full width - 5% padding
```

### Mobile (< 768px)
```
┌──────────────┐
│ [Content]    │
│ (Full width) │
│              │
└──────────────┘
Grid layouts: 1 column
Table display: Scrollable
Modal: 95% width
Font: Adjusted for readability
```

---

## 🎭 Interaction Examples

### Example 1: Earning a Coupon

**Step 1**: Go to Coupons page
```
Screen: Coupons page loads with three panels
```

**Step 2**: Fill Earn Coupon form
```
Customer ID:     CUST001
Booking Ref:     BK-2024-001
Booking Fare:    10000
Travel Date:     2024-12-10 14:30
```

**Step 3**: Click "Earn Coupon"
```
▶ Loading spinner appears
▶ Button disabled
```

**Step 4**: Success
```
✅ Alert: "Coupon earned: ₹300"
▶ Form clears
▶ Dashboard updates automatically
```

### Example 2: Redeeming a Coupon

**Step 1**: Go to Coupons → Click "Redeem Coupon"
```
Modal opens with redemption form
```

**Step 2**: Enter details
```
Customer ID:     CUST001
Booking Ref:     BK-2024-002
Booking Fare:    12000
```

**Step 3**: Drag slider
```
Slider moves → Amount updates: ₹0, ₹2500, ₹5000, etc.
Calculation updates in real-time:
  Booking Fare:    ₹12,000
  Coupon Used:     -₹5,000
  Customer Pays:   ₹7,000
```

**Step 4**: Click "Redeem Coupon"
```
▶ API call sent
▶ Success alert shown
▶ Modal closes
```

---

## 📊 Data Display Patterns

### Metric Cards
```
┌──────────────────────┐
│ LABEL (Gray)         │
│ 4,500 (Large, Bold)  │
│ Subtext (Small)      │
└──────────────────────┘
Used for: Totals, counts, key metrics
```

### Summary Box
```
┌──────────────────────┐
│ Field Name    Value  │
│ Field Name    Value  │
│ ─────────────────    │
│ Total        Value   │ (Bold, larger font)
└──────────────────────┘
Used for: Calculations, totals
```

### Status Badge
```
┌────────┐
│ Status │ (Small text, colored background)
└────────┘
Used for: Status indicators
```

---

## ✨ Special Features & Animations

### Loading States
```
[Spinner Animation]   ← Rotating circle while loading
"Loading..."          ← Text during load
```

### Alerts Auto-Dismiss
```
Alert appears → 4 seconds → Auto closes
User can close manually with [×] button
```

### Modal Animations
```
Overlay: Fade in (0.2s)
Modal: Slide from top (0.3s)
Close: Reverse animation
```

### Hover Effects
```
Buttons: Background darkens
Cards: Box shadow increases
Links: Color changes
```

### Form Validation
```
Focus: Blue border + subtle shadow
Error: Red border + error message
Success: Green checkmark (optional)
Disabled: Gray background, cursor not-allowed
```

---

## 🎯 Key Interaction Patterns

### Pattern 1: View → Action → Confirm
```
View List → Click Action Button → Modal Opens → Fill Form → Submit
→ Loading → Success/Error → Close Modal → Update List
```

### Pattern 2: Quick Lookup
```
Enter Customer ID → Click Search → API Call → Display Results
→ Can perform actions on results
```

### Pattern 3: Live Calculation
```
User Input → Real-time Update → Visual Feedback
(No submit needed, instant calculation)
```

### Pattern 4: Filter & View
```
Display Full List → Type in Filter → Instant Table Update
→ Non-matching rows hidden
```

---

## 🔔 Notification System

### Alert Types & Display
```
✅ SUCCESS (Green)
   Location: Top of content area
   Auto-close: 4 seconds
   Example: "✅ Coupon earned successfully"

❌ ERROR (Red)
   Location: Top of content area
   Auto-close: 4 seconds
   Example: "❌ Customer not found"

⚠️ WARNING (Orange)
   Location: Top of content area
   Auto-close: 4 seconds
   Example: "⚠️ Amount exceeds max redemption"

ℹ️ INFO (Blue)
   Location: Top of content area
   Auto-close: 4 seconds
   Example: "ℹ️ Coupon will be available after travel"
```

---

## 📐 Grid & Spacing System

### Spacing Units
```
Micro:    4px
Small:    8px
Base:     16px (1rem)
Medium:   24px (1.5rem)
Large:    32px (2rem)
X-Large:  48px (3rem)
```

### Grid System
```
- Dashboard: 4-column grid
- Rules: 2-column grid
- Forms: 1-3 column (responsive)
- Responsive: Collapses to 1 column on mobile
```

---

## 🎓 UI Best Practices Used

✅ **Consistent Spacing**: All components follow spacing system  
✅ **Color Coding**: Status indicators use consistent colors  
✅ **Visual Hierarchy**: Title > Subtitle > Content  
✅ **Clear CTAs**: Buttons are clear and actionable  
✅ **Error Prevention**: Validation before submission  
✅ **Feedback**: User always knows what's happening  
✅ **Accessibility**: Good contrast, readable fonts  
✅ **Responsive**: Works on all screen sizes  
✅ **Performance**: Instant feedback, no delays  
✅ **Consistency**: Same patterns throughout  

---

**Frontend UI Guide Complete!**

For detailed code implementation, see: **FRONTEND_GUIDE.md**  
For quick start: **QUICK_START.md**  
For API details: **README.md**

---

**Version**: 1.0  
**Last Updated**: November 2024
