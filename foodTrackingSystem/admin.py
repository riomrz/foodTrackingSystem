from django.contrib import admin
from .models import Product

admin.site.register(Product)

class FoodTrackingSystemAdminArea(admin.AdminSite):
    site_header = 'Food Tracking System Admin Area'

foodTrackingSystem_admin_site = FoodTrackingSystemAdminArea(name="FoodTrackingSystemAdmin")

foodTrackingSystem_admin_site.register(Product)