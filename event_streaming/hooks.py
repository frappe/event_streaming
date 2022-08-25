from . import __version__ as app_version

app_name = "event_streaming"
app_title = "Event Streaming"
app_publisher = "Frappe Technologies"
app_description = "Event Streaming for frappe"
app_email = "hello@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/event_streaming/css/event_streaming.css"
# app_include_js = "/assets/event_streaming/js/event_streaming.js"

# include js, css files in header of web template
# web_include_css = "/assets/event_streaming/css/event_streaming.css"
# web_include_js = "/assets/event_streaming/js/event_streaming.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "event_streaming/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "event_streaming.utils.jinja_methods",
#	"filters": "event_streaming.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "event_streaming.install.before_install"
# after_install = "event_streaming.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "event_streaming.uninstall.before_uninstall"
# after_uninstall = "event_streaming.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "event_streaming.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "*": {
        "after_insert": "event_streaming.event_streaming.doctype.event_update_log.event_update_log.notify_consumers",
        "on_update": "event_streaming.event_streaming.doctype.event_update_log.event_update_log.notify_consumers",
        "on_cancel": "event_streaming.event_streaming.doctype.event_update_log.event_update_log.notify_consumers",
        "on_trash": "event_streaming.event_streaming.doctype.event_update_log.event_update_log.notify_consumers"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"event_streaming.tasks.all"
#	],
#	"daily": [
#		"event_streaming.tasks.daily"
#	],
#	"hourly": [
#		"event_streaming.tasks.hourly"
#	],
#	"weekly": [
#		"event_streaming.tasks.weekly"
#	],
#	"monthly": [
#		"event_streaming.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "event_streaming.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "event_streaming.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "event_streaming.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"event_streaming.auth.validate"
# ]
