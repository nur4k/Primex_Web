from rest_framework import serializers

from apps.news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'created_at', 'views')

    def create(self, validated_data):
        return super().create(validated_data)