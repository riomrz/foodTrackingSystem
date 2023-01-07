from django.contrib import admin
from .models import Product

from django.template.response import TemplateResponse
from django.urls import path

# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('hash', 'txId') # funziona ma poi non mi mostra i campi nemmeno negli oggetti già creati

class FoodTrackingSystemAdminArea(admin.AdminSite):
    site_header = 'Food Tracking System Admin Area'
    
    """ def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('login/', self.admin_site.admin_view(self.custom_login)) # *** RISOLVERE ***
        ]
        return my_urls + urls

    def custom_login(self, request):
        print("get urls custom login")
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           # Anything else you want in the context...
           # key=value,
        )
        return TemplateResponse(request, "sometemplate.html", context) """
    
foodTrackingSystem_admin_site = FoodTrackingSystemAdminArea(name="FoodTrackingSystemAdmin")
foodTrackingSystem_admin_site.register(Product)