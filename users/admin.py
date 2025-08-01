# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['id']

admin.site.register(CustomUser, CustomUserAdmin)
