from django.urls import path

from apps.history.views import HistoryCreateApiView

urlpatterns = [
    path('history-create/', HistoryCreateApiView.as_view())
]
