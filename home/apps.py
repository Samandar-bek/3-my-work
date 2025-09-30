# home/apps.py
from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        import home.signals  # signals faylini ishga tushurish
        # Bu yerda boshqa ishlarni ham bajarish mumkin, masalan, boshlang'ich ma'lumotlarni yuklash