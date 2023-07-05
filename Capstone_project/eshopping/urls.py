from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("item_detail/<int:id>", views.item_detail, name="item_detail"),
    path("item_search", views.item_search, name="item_search"),
    path("view_shopping_cart", views.view_shopping_cart, name="view_shopping_cart"),
    path("placing_order", views.placing_order, name="placing_order"),
    path("user_profile", views.user_profile, name="user_profile"),
    path("staff_view", views.staff_view, name="staff_view"),
    path("protected_view", views.protected_view, name="protected_view"),
    path("order_manage", views.order_manage, name="order_manage"),
    path("customer_detail/<int:user_id>", views.customer_detail, name="customer_detail"),
    path("stock_manage", views.stock_manage, name="stock_manage"),

    # API Routes
    path("page_content/<int:page_no>/<int:category_id>", views.page_content, name="page_content"),
    path("total_page_no_filter/<int:category_id>", views.total_page_no_filter, name="total_page_no_filter"),
    path("search_page_content/<int:page_no>/<str:search_text>", views.search_page_content, name="search_page_content"),
    path("add_shopping_cart/<int:item_id>", views.add_shopping_cart, name="add_shopping_cart"),
    path("edit_shopping_cart_item_no/<int:item_id>", views.edit_shopping_cart_item_no, name="edit_shopping_cart_item_no"),
    path("stock_check/<int:item_id>", views.stock_check, name="stock_check"),
    path("order_detail/<int:order_id>", views.order_detail, name="order_detail")
]