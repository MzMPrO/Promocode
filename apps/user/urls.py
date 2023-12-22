from django.urls import path

from apps.user.views import UserListApiView, UserCreateApiView, UserRetrieveApiView, RegionListApiView

urlpatterns = [
    path('user-list/', UserListApiView.as_view()),
    path('user-create/', UserCreateApiView.as_view()),
    path('user-detail-update/<str:chat_id>/', UserRetrieveApiView.as_view()),
    path('region-list/', RegionListApiView.as_view()),
]
