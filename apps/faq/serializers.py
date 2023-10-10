from rest_framework import serializers

from apps.faq.models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'title', 'description')

    def create(self, validated_data):
        return super().create(validated_data)

