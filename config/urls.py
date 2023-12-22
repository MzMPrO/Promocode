from django.contrib import admin
from django.urls import path, include

from config.swagger import schema_view

urlpatterns = [
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
