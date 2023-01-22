from django.apps import AppConfig
# from django.contrib.admin.apps import AdminConfig

""" class FoodTrackingSystemAdminConfig(AdminConfig):
    default_site = 'foodTrackingSystem.admin.FoodTrackingSystemAdminArea'
 """

class FoodTrackingSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foodTrackingSystem'
