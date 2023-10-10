from rest_framework import serializers

from apps.services.models import Service


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'icon')

    def create(self, validated_data):
        return super().create(validated_data)