from rest_framework import serializers

from apps.promocode.models import Promocode
from apps.user.models import User


class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = ['promocode', 'price', 'is_active']


class PromocodeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = ['is_active']
