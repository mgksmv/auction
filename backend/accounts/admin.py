from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    def full_name(self, obj):
        return str(obj)

    list_display = ('email', 'full_name', 'birthday')
    ordering = ('email',)
    list_filter = ()
    fieldsets = ()
