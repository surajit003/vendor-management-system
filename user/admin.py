from django.contrib import admin
from .models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_id', 'first_name', 'last_name',)
