from rest_framework.routers import DefaultRouter

from apps.about_as.views import About_AsView


router = DefaultRouter()
router.register('about_as', About_AsView)

urlpatterns = []
urlpatterns += router.urls