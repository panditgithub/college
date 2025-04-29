from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import Group

from .forms import UserCreationForm
from .models import User, ContactMessage


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm  # For creating users in admin
    model = User  # Required to register the correct model

    list_display = (
        'email', 'first_name', 'username1',
        'enrollment_number', 'course', 'year'
    )
    list_filter = ('course', 'branch', 'year', 'is_admin')

    fieldsets = (
        (None, {'fields': ('email', 'password', 'username1')}),
        ('Personal info', {
            'fields': (
                'first_name', 'last_name', 'enrollment_number', 'course',
                'branch', 'year', 'phone', 'profile_picture','registration','valid'
            )
        }),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'username1',
                'enrollment_number', 'course', 'branch', 'year',
                'phone', 'profile_picture', 'password1', 'password2','registration','valid'
            ),
        }),
    )

    search_fields = ('email', 'first_name', 'enrollment_number')
    ordering = ('email',)
    filter_horizontal = ()  # You can keep this empty


# Register the models
admin.site.register(User, UserAdmin)
admin.site.register(ContactMessage)

# Optional: Unregister Group if you don't use default groups/permissions
# admin.site.unregister(Group)
