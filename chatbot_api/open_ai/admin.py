from django.contrib import admin
from open_ai.models import Chat

# Register your models here.
@admin.register(Chat)
class Chat(admin.ModelAdmin):
    pass
    # fieldsets = (
    #     ('Credentials', {'fields': ('username', 'password')}),
    #     ('Personal information', {'fields': ('email', 'first_name', 'last_name')}),
    # )
    # list_display = ['email', 'date_joined']
