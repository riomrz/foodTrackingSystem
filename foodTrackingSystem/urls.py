from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.insert_code, name='insert_code'),
    path('product/', views.product_detail, name='product_detail'),
]

urlpatterns += staticfiles_urlpatterns()