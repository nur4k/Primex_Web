from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.news.views import NewsView


router = DefaultRouter()
router.register('news', NewsView)

urlpatterns = []
urlpatterns += router.urls