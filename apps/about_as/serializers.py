from rest_framework import serializers

from apps.about_as.models import About_As, FeedBack


class About_asSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_As
        fields = ('id', 'title', 'description')

    def create(self, validated_data):
        return super().create(validated_data)


class FeedBackSerialzier(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ('id', 'fio', 'email', 'number', 'theme',
                    'title', 'description')
        
    def create(self, validated_data):
        return super().create(validated_data)
