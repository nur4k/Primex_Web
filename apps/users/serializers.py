from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'role', 'phone_number', 'address_delivery')

    def create(self, validated_data):
        return super().create(validated_data)
