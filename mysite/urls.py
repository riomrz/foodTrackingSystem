from django.contrib import admin
from django.urls import path, include
from foodTrackingSystem.admin import foodTrackingSystem_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodTrackingSystemAdmin/', foodTrackingSystem_admin_site.urls),
    path('', include('foodTrackingSystem.urls')),
]
