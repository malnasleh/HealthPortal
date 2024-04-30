from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering=['healthID']
    list_display = ["healthID",]
    fieldsets = (
        (None, {'fields': ('healthID', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'Age', 'Phone_num', 'Address')}),
        (('User Type'), {'fields': ('userKind',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('healthID', 'password1', 'password2'),
        }), 
        (('Personal info'), {'fields': ('first_name', 'last_name', 'Age', 'Phone_num', 'Address')}),
        (('User Type'), {'fields': ('userKind',)}),
    )

    # fieldsets = UserAdmin.fieldsets + (
    #     (
    #         'Contact Info',
    #         {
    #             'fields': (
    #                 'Age', 'Phone_num', 'Address'
    #             ),
    #         },
    #     ),
    # ) + (
    #     (
    #         'Type of User',
    #         {
    #             'fields': (
    #                 'is_patient',
    #             ),
    #         },
    #     ),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (('Personal Information', {'fields': (
    #     'Age', 'Phone_num', 'Address'), },),) + (('Type of User', {'fields': ('is_patient',), },),)


admin.site.register(CustomUser, CustomUserAdmin)
