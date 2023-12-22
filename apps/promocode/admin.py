from django.contrib import admin
from apps.promocode.models import Promocode
from import_export.admin import ImportExportModelAdmin


class PromocodeAdmin(ImportExportModelAdmin):
    list_display = ('promocode', 'price', 'is_active', 'created_at')
    search_fields = ('promocode', 'created_at')
    list_filter = ('is_active', 'created_at')


admin.site.register(Promocode, PromocodeAdmin)
