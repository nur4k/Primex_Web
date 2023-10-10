from rest_framework import serializers

from apps.main_page.models import MainPage


class Main_PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = ('id', 'title', 'description')

    def create(self, validated_data):
        return super().create(validated_data)
    