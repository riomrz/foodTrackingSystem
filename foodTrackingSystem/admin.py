from django.contrib import admin
from .models import Product

from django.template.response import TemplateResponse
from django.urls import path

from foodTrackingSystem import models

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('hash', 'txId') # funziona ma poi non mi mostra i campi nemmeno negli oggetti già creati

class FoodTrackingSystemAdminArea(admin.AdminSite):
    site_header = 'Food Tracking System Admin Area'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('', self.admin_view(self.log_on_redis)) # *** RISOLVERE ***
        ]
        return my_urls + urls

    def log_on_redis(self, request):
        print("log on redis")
        context = dict(
           # Include common variables for rendering the admin template.
           self.each_context(request),
           # Anything else you want in the context...
           # key=value,
        )
        print("context: ", context)
        return TemplateResponse(request, "admin/base_site.html", context) # FUNZIONA solo se lo mando su admin/base.html
    
foodTrackingSystem_admin_site = FoodTrackingSystemAdminArea(name="FoodTrackingSystemAdmin")
foodTrackingSystem_admin_site.register(models.Product)