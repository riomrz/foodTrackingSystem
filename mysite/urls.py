from django.contrib import admin
from django.urls import path, include
from foodTrackingSystem.admin import foodTrackingSystem_admin_site

""" A STAFF STATUS ADMIN IS SUPPOSED TO USE THE foodTrackingSystemAdmin/ PAGE
in order to add new products.
admin/ page is left as default in order to let a superuser to be able to access it.
A user with superuser privileges can access admin/ page with all permissions, 
while a user with staff status can access only the foodTrackingSystemAdmin/ page 
and add products. """

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodTrackingSystemAdmin/', foodTrackingSystem_admin_site.urls),
    path('', include('foodTrackingSystem.urls')),
]
