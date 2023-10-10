from rest_framework.viewsets import ModelViewSet

from apps.about_as.models import About_As
from apps.about_as.serializers import About_asSerializer


class About_AsView(ModelViewSet):
    queryset = About_As.objects.all()
    serializer_class = About_asSerializer
