from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.promocode.models import Promocode
from apps.promocode.serializers import PromocodeSerializer, PromocodeUpdateSerializer


class PromocodeListApiView(ListAPIView):
    serializer_class = PromocodeSerializer
    queryset = Promocode.objects.all()


class PromocodeUpdateApiView(UpdateAPIView):
    serializer_class = PromocodeUpdateSerializer
    lookup_field = 'promocode'
    queryset = Promocode.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class PromocodeRetrieveApiView(RetrieveAPIView):
    serializer_class = PromocodeSerializer
    queryset = Promocode.objects.all()
    lookup_field = 'promocode'
