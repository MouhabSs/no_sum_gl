# No Sum GL

A comprehensive Frappe/ERPNext application that provides detailed General Ledger reports without entry summarization, including full audit-ready print capabilities with bilingual (English/Arabic) support.

## The Problem

ERPNext's standard General Ledger report aggregates multiple entries of the same account from a single voucher into one summarized row. For example, if a Journal Entry has three separate debit lines for "Cash" (50,000 + 30,000 + 20,000), the standard GL report collapses them into a single row showing 100,000.

This makes it impossible to audit individual line items as they were originally entered, and creates compliance challenges for financial reporting.

## The Solution

**No Sum GL** provides two comprehensive reports:

### 1. **GL Report View** - Interactive Report
Queries the `GL Entry` table directly without any grouping or aggregation, displaying every line item exactly as it was posted with full filtering capabilities.

### 2. **Statement of Account** - Printable Statement
A professional, bilingual (English/Arabic) statement of account with company logo, signatures section, and complete audit trail.

## Features

### GL Report View
- ✅ Individual GL line items without summarization
- ✅ Advanced filters: Company, Date Range, Account, Voucher No, Cost Center, Party Type, Party
- ✅ Optional Remarks column
- ✅ Accounting Dimensions support
- ✅ Finance Book filtering
- ✅ Invoice and Print functionality

### Statement of Account
- ✅ Professional print-ready format (HTML/PDF)
- ✅ Bilingual headers (English & Arabic)
- ✅ Company logo display
- ✅ Signature section in footer for approvals
- ✅ Running balance calculation
- ✅ Full GL entry details (Date, Account, Party, Voucher, Debit, Credit, Balance)
- ✅ Optional remarks column
- ✅ Print optimization with proper styling
- ✅ Currency formatting with company default

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

### 1. Get the app:
```bash
cd /home/frappe/frappe-bench
bench get-app https://github.com/yourusername/no_sum_gl.git
```

### 2. Install on your site:
```bash
bench --site your-site-name install-app no_sum_gl
```

### 3. Run migrations:
```bash
bench --site your-site-name migrate
```

### 4. Restart bench:
```bash
bench restart
```

## Usage

After installation, the **GL Report View** shortcut appears automatically in the **Accounting** workspace.

### Running the GL Report View
1. Navigate to **Accounting Workspace**
2. Click **GL Report View** shortcut
3. Set filters:
   - **Company** (mandatory)
   - **From Date** and **To Date**
   - Optional: Account, Voucher No, Cost Center, Party, Party Type
   - Check "Show Remarks" to include transaction remarks
   - Check "Consider Accounting Dimensions" for dimension filtering
   - Check "Include Default FB Entries" for Finance Book entries

### Printing a Statement of Account
1. Run the GL Report View with desired filters
2. Click **Print Statement** button
3. Configure company logo (see below)
4. Document opens in print preview
5. Print or save as PDF

### Setting Up Company Logo

The Statement of Account automatically displays your company logo. To add one:

1. Go to **Setup → Company** (select your company)
2. In the **Company** form, find the **Logo** field
3. Upload your company logo (PNG/JPG format)
4. Click **Save**
5. The logo will now appear in all Statement of Account prints

**Logo Guidelines:**
- Format: PNG or JPG
- Recommended size: 200x150 pixels
- Max height in print: 80px

## Features Overview

### Report Filters
- **Company**: Required. Select the company for the GL entries
- **Date Range**: Required. Filter by posting date
- **Account**: Optional. Filter by specific GL account
- **Voucher No**: Optional. Filter by document reference number
- **Cost Center**: Optional. Filter by cost center
- **Party Type**: Optional. Filter by customer/supplier/employee
- **Party**: Optional. Filter by specific party name
- **Show Remarks**: Optional. Include transaction remarks in print
- **Accounting Dimensions**: Optional. Filter by custom dimensions
- **Finance Book**: Optional. Filter by finance book

### Print Output
- Bilingual headers (English/Arabic)
- Company information
- Date range
- Account and party details
- Complete transaction listing with:
  - Posting Date
  - Account
  - Party Type & Party
  - Voucher Type & Number
  - Debit & Credit amounts
  - Running balance
  - Cost Center
  - Remarks (optional)
- Signature lines for:
  - General Manager
  - Financial Manager
  - Accounts Manager
- Print timestamp

## Permissions

The reports are available to users with:
- **Accounts User**
- **Accounts Manager**
- **Auditor**

## Development

### Project Structure
```
no_sum_gl/
├── no_sum_gl/
│   ├── report/
│   │   ├── gl_report_view/
│   │   │   ├── gl_report_view.py
│   │   │   ├── gl_report_view.js
│   │   │   ├── gl_report_view.json
│   │   │   └── gl_report_view.html
│   │   └── statement_of_account/
│   ├── hooks.py
│   ├── setup.py
│   └── __init__.py
├── .gitignore
├── pyproject.toml
└── README.md
```

### Contributing
Contributions are welcome! Please ensure:
- Code follows PEP 8 standards
- All filters and features are tested
- Documentation is updated

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or feature requests, please create an issue on the project repository.

---

**Version**: 1.0.0  
**Last Updated**: April 2026  
**Author**: Mo