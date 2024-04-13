from django.contrib import admin
from .models import Bannersection

# Register your models here.
class AdminHappyBannersection(admin.ModelAdmin):
    list_display=('Id','Title','CreatedName','Create_at')
    list_filter = ["CreatedName",'Create_at']

admin.site.register(Bannersection,AdminHappyBannersection)