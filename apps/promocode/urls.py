from django.urls import path

from apps.promocode.views import PromocodeListApiView, PromocodeUpdateApiView, PromocodeRetrieveApiView

urlpatterns = [
    path('promocode-list/', PromocodeListApiView.as_view()),
    path('promocode-update/<str:promocode>', PromocodeUpdateApiView.as_view()),
    path('promocode-detail/<str:promocode>', PromocodeRetrieveApiView.as_view()),
]
