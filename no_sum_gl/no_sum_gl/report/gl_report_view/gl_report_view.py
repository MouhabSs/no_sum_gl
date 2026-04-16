# Copyright (c) 2026, Mo and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    if not filters:
        filters = {}

    conditions = ["gle.is_cancelled = 0"]
    values = {}

    if filters.get("company"):
        conditions.append("gle.company = %(company)s")
        values["company"] = filters["company"]
    if filters.get("from_date"):
        conditions.append("gle.posting_date >= %(from_date)s")
        values["from_date"] = filters["from_date"]
    if filters.get("to_date"):
        conditions.append("gle.posting_date <= %(to_date)s")
        values["to_date"] = filters["to_date"]
    if filters.get("account"):
        conditions.append("gle.account = %(account)s")
        values["account"] = filters["account"]
    if filters.get("voucher_no"):
        conditions.append("gle.voucher_no = %(voucher_no)s")
        values["voucher_no"] = filters["voucher_no"]
    if filters.get("cost_center"):
        conditions.append("gle.cost_center = %(cost_center)s")
        values["cost_center"] = filters["cost_center"]
    if filters.get("party_type"):
        conditions.append("gle.party_type = %(party_type)s")
        values["party_type"] = filters["party_type"]
    if filters.get("party"):
        conditions.append("gle.party = %(party)s")
        values["party"] = filters["party"]

    # Include Default Finance Book Entries
    if filters.get("include_default_fb_entries"):
        default_fb = frappe.db.get_value(
            "Company", filters.get("company"), "default_finance_book"
        )
        if default_fb:
            conditions.append(
                "(gle.finance_book = %(finance_book)s OR gle.finance_book IS NULL OR gle.finance_book = '')"
            )
            values["finance_book"] = default_fb
        else:
            conditions.append("(gle.finance_book IS NULL OR gle.finance_book = '')")

    # Consider Accounting Dimensions
    if filters.get("consider_accounting_dimensions"):
        accounting_dimensions = frappe.get_all(
            "Accounting Dimension", pluck="fieldname"
        )
        for dim in accounting_dimensions:
            if filters.get(dim):
                conditions.append("gle.`{0}` = %({0})s".format(dim))
                values[dim] = filters[dim]

    where_clause = " AND ".join(conditions)

    # Always present columns
    columns = [
        {"label": "Posting Date", "fieldname": "posting_date", "fieldtype": "Date", "width": 110},
        {"label": "Account", "fieldname": "account", "fieldtype": "Link", "options": "Account", "width": 220},
        {"label": "Party Type", "fieldname": "party_type", "fieldtype": "Data", "width": 100},
        {"label": "Party", "fieldname": "party", "fieldtype": "Data", "width": 150},
        {"label": "Voucher Type", "fieldname": "voucher_type", "fieldtype": "Data", "width": 110},
        {"label": "Voucher No", "fieldname": "voucher_no", "fieldtype": "Dynamic Link", "options": "voucher_type", "width": 160},
        {"label": "Debit", "fieldname": "debit", "fieldtype": "Currency", "width": 120},
        {"label": "Credit", "fieldname": "credit", "fieldtype": "Currency", "width": 120},
        {"label": "Cost Center", "fieldname": "cost_center", "fieldtype": "Link", "options": "Cost Center", "width": 150},
    ]

    select_fields = """
        gle.posting_date,
        gle.account,
        gle.party_type,
        gle.party,
        gle.voucher_type,
        gle.voucher_no,
        gle.debit,
        gle.credit,
        gle.cost_center
    """


    # Show Remarks — add column and select field only if checked
    if filters.get("show_remarks"):
        columns.append(
            {"label": "Remarks", "fieldname": "remarks", "fieldtype": "Data", "width": 150}
        )
        select_fields += ", gle.remarks"

    data = frappe.db.sql("""
        SELECT {select_fields}
        FROM `tabGL Entry` gle
        WHERE {where_clause}
        ORDER BY gle.posting_date, gle.voucher_no, gle.name
    """.format(select_fields=select_fields, where_clause=where_clause), values, as_dict=True)

    return columns, data

@frappe.whitelist()
def get_print_data(filters):
    if isinstance(filters, str):
        import json
        filters = json.loads(filters)

    try:
        columns, data = execute(filters)

        company_doc = frappe.get_doc("Company", filters.get("company"))
        
        # Handle logo URL
        logo_url = ""
        if company_doc.company_logo:
            logo_path = company_doc.company_logo
            # If it's a relative path, construct the full URL
            if not logo_path.startswith("http"):
                logo_url = frappe.utils.get_url(logo_path)
            else:
                logo_url = logo_path

        html = frappe.render_template(
            "no_sum_gl/no_sum_gl/report/gl_report_view/gl_report_view.html",
            {
                "data": data,
                "filters": filters,
                "company": company_doc,
                "logo": logo_url,
                "from_date": filters.get("from_date"),
                "to_date": filters.get("to_date"),
                "party": filters.get("party", ""),
                "party_type": filters.get("party_type", ""),
                "account": filters.get("account", ""),
                "show_remarks": filters.get("show_remarks"),
                "currency": company_doc.default_currency or "EGP",
                "print_date": frappe.utils.now_datetime().strftime("%d-%m-%Y %H:%M:%S")
            }
        )
        
        return {
            "html": html,
            "message": "success"
        }
    except Exception as e:
        frappe.log_error(f"Error in get_print_data: {str(e)}", "GL Report View Print")
        return {
            "html": f"<h1>Error generating print</h1><p>{str(e)}</p>",
            "message": "error",
            "error": str(e)
        }