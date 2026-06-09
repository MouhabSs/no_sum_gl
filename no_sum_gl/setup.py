import frappe

def add_workspace_shortcut():
    workspace_name = "Accounting"

    # Wait — report must exist before we can link to it
    if not frappe.db.exists("Report", "GL Report View"):
        return

    existing = frappe.db.exists(
        "Workspace Shortcut",
        {"label": "GL Report View", "parent": workspace_name}
    )
    if existing:
        return

    workspace = frappe.get_doc("Workspace", workspace_name)
    workspace.append("shortcuts", {
        "label": "GL Report View",
        "type": "Report",
        "link_to": "GL Report View",
        "format": "pill",
        "color": "#2490EF",
        "icon": "ledger"
    })
    workspace.save(ignore_permissions=True)
    frappe.db.commit()