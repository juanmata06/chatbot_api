from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Credentials', {'fields': ('username', 'password')}),
        ('Personal information', {'fields': ('email', 'first_name', 'last_name')}),
    )
    list_display = ['email', 'date_joined']