from django.urls import path
from . import views

app_name="klaxonKitchen"
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.dashboard, name="home"),
    path('add_kitchen', views.add_kitchen, name="add_kitchen"),
    path('add_order', views.add_order, name="add_order"),
    path('kitchen/<int:kitchen_id>', views.kitchenDashboard, name="kitchen"),
    path('update_order_status/<int:order_id>', views.update_order_status, name="update_order_status"),
    path('all_orders', views.all_orders, name="all_orders"),
    path('display_screen', views.display_screen, name="display_screen"),
    path('export_orders', views.export_orders, name="export_orders"),
    path('export_kitchens', views.export_kitchens, name="export_kitchens"),
    path('delete_order/<int:order_id>', views.delete_order, name="delete_orders"),
    path('reset_counter_all', views.reset_counter_all),
    path('settings', views.settings, name="settings"),
]
