from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, GenericAPIView
from rest_framework.response import Response

from apps.user.models import User, Region
from apps.user.serializers import UserListSerializer, UserCreateSerializer, RegionListSerializer


class UserListApiView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class UserCreateApiView(GenericAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()

        return Response(result, status=status.HTTP_201_CREATED)


class UserRetrieveApiView(RetrieveUpdateAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    lookup_field = 'chat_id'

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class RegionListApiView(ListAPIView):
    serializer_class = RegionListSerializer
    queryset = Region.objects.all()
