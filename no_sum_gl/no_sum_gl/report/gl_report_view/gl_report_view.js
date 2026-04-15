// Copyright (c) 2026, Mo and contributors
// For license information, please see license.txt

frappe.query_reports["GL Report View"] = {
    filters: [
        {
            fieldname: "company",
            label: __("Company"),
            fieldtype: "Link",
            options: "Company",
            mandatory: 1,
            default: frappe.defaults.get_user_default("Company")
        },
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            mandatory: 1,
            default: frappe.datetime.add_months(frappe.datetime.nowdate(), -1)
        },
        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date",
            mandatory: 1,
            default: frappe.datetime.nowdate()
        },
        {
            fieldname: "account",
            label: __("Account"),
            fieldtype: "Link",
            options: "Account"
        },
        {
            fieldname: "voucher_no",
            label: __("Voucher No"),
            fieldtype: "Data"
        },
        {
            fieldname: "cost_center",
            label: __("Cost Center"),
            fieldtype: "Link",
            options: "Cost Center"
        },
        {
            fieldname: "party_type",
            label: __("Party Type"),
            fieldtype: "Select",
            options: "\nCustomer\nSupplier\nEmployee"
        },
        {
            fieldname: "party",
            label: __("Party"),
            fieldtype: "Data"
        },
        {
            fieldname: "show_remarks",
            label: __("Show Remarks"),
            fieldtype: "Check",
            default: 0
        },
        {
            fieldname: "consider_accounting_dimensions",
            label: __("Consider Accounting Dimensions"),
            fieldtype: "Check",
            default: 1
        },
        {
            fieldname: "include_default_fb_entries",
            label: __("Include Default FB Entries"),
            fieldtype: "Check",
            default: 1
        }
    ],
    onload: function(report) {
        report.page.add_inner_button(__("Print Statement"), function() {
            let filters = report.get_values();

            if (!filters.company) {
                frappe.msgprint(__("Please select a Company first"));
                return;
            }

            frappe.call({
                method: "no_sum_gl.report.gl_report_view.gl_report_view.get_print_data",
                args: { filters: filters },
                callback: function(r) {
                    if (!r.message) {
                        frappe.msgprint(__("Error: No response from server"));
                        return;
                    }
                    
                    let html = r.message.html || r.message;
                    
                    if (r.message.error) {
                        frappe.msgprint(__("Error generating print: " + r.message.error));
                        return;
                    }
                    
                    let w = window.open();
                    w.document.write(html);
                    w.document.close();
                    setTimeout(() => { w.print(); }, 1000);
                }
            });
        });
    }
};