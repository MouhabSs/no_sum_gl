# No Sum GL

A Frappe/ERPNext application that provides a detailed General Ledger report without entry summarization.

## The Problem

ERPNext's standard General Ledger report aggregates multiple entries of the same account from a single voucher into one summarized row. For example, if a Journal Entry has three separate debit lines for "Cash" (50,000 + 30,000 + 20,000), the standard GL report collapses them into a single row showing 100,000.

This makes it impossible to audit individual line items as they were originally entered.

## The Solution

**No Sum GL** adds a new report — **GL Report View** — that queries the `GL Entry` table directly without any grouping or aggregation, displaying every line item exactly as it was posted.

## Features

- Individual GL line items without summarization
- Filters for Company, Date Range, Account, Voucher No, Cost Center, Party Type, and Party
- Optional Remarks column via "Show Remarks" checkbox
- Accounting Dimensions support
- Finance Book filtering
- Compatible with ERPNext v15

## Requirements

| Requirement | Version |
|---|---|
| Frappe Framework | v15.x |
| ERPNext | v15.x |
| Python | 3.10+ |
| MariaDB | 10.6+ |
| Node.js | 18+ |

## Installation

Make sure you have a working Frappe bench with ERPNext installed.

**1. Get the app:**
```bash
cd /home/frappe/frappe-bench
bench get-app 
```

**2. Install on your site:**
```bash
bench --site your-site-name install-app no_sum_gl
```

**3. Run migrations:**
```bash
bench --site your-site-name migrate
```

**4. Restart bench:**
```bash
bench restart
```

## Usage

After installation, navigate to:

**GL Report View**

## Permissions

## License

MIT