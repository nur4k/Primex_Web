from rest_framework.viewsets import ModelViewSet

from apps.news.models import News
from apps.news.serializers import NewsSerializer


class NewsView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        for obj in queryset:
            if obj.views is None:
                obj.views = 0
            obj.views += 1
            obj.save()
        return queryset
