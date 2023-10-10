from rest_framework.routers import DefaultRouter

from apps.services.views import ServiceView


router = DefaultRouter()
router.register('services', ServiceView)

urlpatterns = []
urlpatterns += router.urls