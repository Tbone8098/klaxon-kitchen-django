from django.urls import path
from . import views

app_name="klaxonKitchen"
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.dashboard, name="home"),
    path('add_kitchen', views.add_kitchen, name="add_kitchen"),
    path('add_order', views.add_order, name="add_order"),
    path('kitchen/<int:kitchen_id>', views.kitchenDashboard, name="kitchen"),
    path('kitchen/delete/<int:kitchen_id>', views.kitchenDelete, name="kitchen_delete"),
    path('kitchen/delete/confirm/<int:kitchen_id>', views.kitchenDeleteConfirm, name="kitchen_delete_confirm"),
    path('update_order_status/<int:order_id>', views.update_order_status, name="update_order_status"),
    path('all_orders', views.all_orders, name="all_orders"),
    path('display_screen', views.display_screen, name="display_screen"),
    path('export_orders', views.export_orders, name="export_orders"), 
    path('export_kitchens', views.export_kitchens, name="export_kitchens"),
    path('delete_order/<int:order_id>', views.deleteOrder, name="delete_orders"),
    path('delete_order/confirm/<int:order_id>', views.deleteOrderConfirm, name="delete_orders_confirm"),
    path('reset_counter_all', views.reset_counter_all, name="reset_counters"),
    path('settings', views.settings, name="settings"),
    path('order_details/<int:order_id>', views.order_details, name="order_details"),
    path('order_update/<int:order_id>', views.order_update, name="order_update"),
]
