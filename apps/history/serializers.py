from rest_framework import serializers
from apps.history.models import History
from apps.user.models import User, Region
from apps.promocode.models import Promocode


class HistoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(default='')
    promocode = serializers.CharField(default='')

    class Meta:
        model = History
        fields = ['user', 'promocode']

    def create(self, validated_data):
        History.objects.create(user=User.objects.get(chat_id=validated_data['user']),
                               promocode=Promocode.objects.get(promocode=validated_data['promocode'])
        )
        return {}
