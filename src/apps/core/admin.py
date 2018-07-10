from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_filter = ('created', 'is_staff', 'is_superuser', 'groups')
    list_display = []
    fieldsets = (
        (
            None,
            {'fields': ('email', 'password')}
         ),
        (
            u'Información personal',
            {
                'fields': ('first_name', 'last_name', 'dni', 'tlf', 'address', 'birth_date', )
             }
         ),
        (
            'Accesos',
            {'fields': ('is_staff', 'is_superuser')}
         ),
        ('Permisos', {
             'fields': ('user_permissions', )
         }),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'tlf', 'dni')
    ordering = ('-points',)
    filter_horizontal = ('groups', 'user_permissions',)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return (
                'email', 'password', 'first_name', 'last_name', 'dni', 'tlf', 'address', 'birth_date',
                'is_staff', 'user_permissions', 'is_superuser'
            )
        return super().get_readonly_fields(request, obj)

    def get_list_display(self, request, obj=None):
        fields = ['get_full_name', 'created', 'is_staff']
        if request.user.is_superuser:
            fields.append('points')
        return fields



admin.site.unregister(Group)
