from rest_framework.viewsets import ModelViewSet

from apps.partners.models import Partner
from apps.partners.serializers import PartnerSerialzier


class PartnerView(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerialzier
