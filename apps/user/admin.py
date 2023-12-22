from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.user.models import User, Region


class UserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'full_name', 'phone_number', 'region')
    search_fields = ('chat_id', 'full_name', 'phone_number', 'region')


class RegionAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(User, UserAdmin)
admin.site.register(Region, RegionAdmin)
