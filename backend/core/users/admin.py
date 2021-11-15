from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Package, ServiceFeedBack


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm #<-- modify the fields from here
    model = CustomUser
    list_display = ('email', 'credit', 'duration', 'package', 'date_joined', 'is_staff', 'is_active',)
    list_filter = ('email', 'credit', 'duration', 'package', 'date_joined', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'credit', 'duration', 'package')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'credit', 'duration', 'package', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Package)
admin.site.register(ServiceFeedBack)