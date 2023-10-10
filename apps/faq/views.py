from rest_framework.viewsets import ModelViewSet

from apps.faq.models import FAQ
from apps.faq.serializers import FAQSerializer


class FAQView(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
