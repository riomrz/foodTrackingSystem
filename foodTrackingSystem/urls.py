from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.insert_code, name='insert_code'),
]

urlpatterns += staticfiles_urlpatterns()