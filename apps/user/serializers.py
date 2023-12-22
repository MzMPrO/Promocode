from rest_framework import serializers

from apps.user.models import User, Region


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['chat_id', 'full_name', 'phone_number', "region", 'balance']


class UserCreateSerializer(serializers.ModelSerializer):
    region = serializers.CharField(default='')

    class Meta:
        model = User
        fields = ['chat_id', 'full_name', 'phone_number', "region"]

    def create(self, validated_data):
        User.objects.create(chat_id=validated_data['chat_id'],
                            full_name=validated_data['full_name'],
                            phone_number=validated_data['phone_number'],
                            region=Region.objects.get(name=validated_data['region']))
        return {}


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", 'name']
