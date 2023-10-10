from rest_framework.viewsets import ModelViewSet

from apps.services.models import Service
from apps.services.serializers import ServicesSerializer


class ServiceView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
