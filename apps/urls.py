from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('', include('apps.user.urls')),
    path('', include('apps.history.urls')),
    path('', include('apps.promocode.urls')),
]
