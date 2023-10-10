from rest_framework.viewsets import ModelViewSet

from apps.main_page.models import MainPage
from apps.main_page.serializers import Main_PageSerializer



class Main_PageView(ModelViewSet):
    queryset = MainPage.objects.all()
    serializer_class = Main_PageSerializer