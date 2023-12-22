from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.history.serializers import HistoryCreateSerializer


class HistoryCreateApiView(GenericAPIView):
    serializer_class = HistoryCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()

        return Response(result, status=status.HTTP_201_CREATED)
