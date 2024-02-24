from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    ordering = ["username"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    exclude = ('date_joined',)
    list_display = ["username", "email", "first_name", "last_name", "is_staff", "is_active"]
    list_display_links = ["username"]
    list_filter = ["username", "email", "first_name", "last_name", "is_staff", "is_active"]
    search_fields = ["username", "email", "first_name", "last_name"]
    fieldsets = (
        ('Login Credentials', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    
admin.site.register(User, UserAdmin)