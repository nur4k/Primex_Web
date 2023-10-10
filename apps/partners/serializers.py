from rest_framework import serializers

from apps.partners.models import Partner


class PartnerSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'logo', 'address', 'contacts')

    def create(self, validated_data):
        return super().create(validated_data)
