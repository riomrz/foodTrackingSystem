import redis
from django.contrib import admin, messages
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import path

from foodTrackingSystem import models

from .models import Product


SERVER_IP = '127.0.0.1'
SERVER_PORT = '6379'
PASSWORD = ''
DB = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['code', 'hash', 'txId'] # not working

class FoodTrackingSystemAdminArea(admin.AdminSite):
    site_header = 'Food Tracking System Admin Area'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('', self.admin_view(self.log_on_redis))
        ]
        return my_urls + urls

    def log_on_redis(self, request):
        # create context to return template
        context = dict(
           # Include common variables for rendering the admin template.
           self.each_context(request),
           # Anything else you want in the context...
           # key=value,
        )

        # check ip (redis client errors don't break the app)
        try:
            client = redis.StrictRedis(host=SERVER_IP, 
                                    port=SERVER_PORT, 
                                    password=PASSWORD,
                                    db=DB,
                                    charset="utf-8", 
                                    decode_responses=True)
            current_ip = request.META['REMOTE_ADDR']
            user_email = request.user.email # users must have an email
            last_ip = client.get(user_email)
            if current_ip != last_ip:
                client.set(user_email, current_ip)
                messages.add_message(request, messages.INFO, 'IP address is changed')
        except redis.exceptions.RedisError:
            print("No Redis client")
            return render(request, 'foodTrackingSystem/login_error.html')
        except:
            print("Exception in log_on_redis custom admin method")
            return render(request, 'foodTrackingSystem/login_error.html')

        return TemplateResponse(request, "admin/base_site.html", context) # works only sending the user on admin/base.html
    
foodTrackingSystem_admin_site = FoodTrackingSystemAdminArea(name="FoodTrackingSystemAdmin")
foodTrackingSystem_admin_site.register(models.Product)