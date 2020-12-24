from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.dashboard),
    path('add_kitchen', views.add_kitchen),
    path('add_order', views.add_order),
    path('kitchen/<int:kitchen_id>', views.kitchenDashboard),
    path('update_order_status/<int:order_id>', views.update_order_status),
    path('all_orders', views.all_orders),
    path('display_screen', views.display_screen),
    path('export_orders', views.export_orders),
    path('export_kitchens', views.export_kitchens),
    path('delete_order/<int:order_id>', views.delete_order)
]
