from django.contrib import admin
from apps.history.models import History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'promocode', 'created_at')
    search_fields = ('promocode', 'user')


admin.site.register(History, HistoryAdmin)
