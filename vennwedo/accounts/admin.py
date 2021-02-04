from django.contrib import admin
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = CustomUser
    list_display = ('username','name', 'email',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )


# admin.site.register(CustomUser, UserAdminConfig)
