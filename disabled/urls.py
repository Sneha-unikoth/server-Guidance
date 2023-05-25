from django.urls import path
from disabled import views

urlpatterns = [
    path("",views.admin_login,name="admin_login"),
    path("dashboard",views.admin_dashboard,name="admin_dashboard"),
    path("approveshop",views.admin_approveshop,name="admin_approveshop"),
    path("complaints",views.admin_complaints,name="admin_complaints"),
    path("feedback",views.admin_feedback,name="admin_feedback"),
    path("managecounciling",views.admin_managecounciling,name="admin_managecounciling"),
    path("manageshop",views.admin_manageshop,name="admin_manageshop"),
    path("manageusers",views.admin_manageusers,name="admin_manageusers"),
    path("notification",views.admin_notification,name="admin_notification"),
    path("product",views.admin_product,name="admin_product"),
    path("viewuser",views.admin_viewuser,name="admin_viewuser"),
    path("notification",views.notification,name="notification"),

    path("admin_approve_users/<int:id>",views.admin_approve_users,name="admin_approve_users"),
    path("admin_delete_user/<int:id>",views.admin_delete_user,name="admin_delete_user"),
    path("admin_approveshop/<int:id>",views.admin_approve_shop,name="admin_approveshop"),
    path("admin_delete_user/<int:id>",views.admin_delete_user,name="admin_delete_user"),
    path("admin_delete_shop/<int:id>",views.admin_delete_shop,name="admin_delete_shop"),
    path("admin_view_product",views.admin_view_product,name="admin_view_product"),
    path("admin_view_feedback",views.admin_view_feedback,name="admin_view_feedback"),
    path("admin_view_complaints",views.admin_view_complaints,name="admin_view_complaints"),
    path("admin_view_notification",views.admin_view_notification,name="admin_view_notification"),
]


