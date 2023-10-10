from rest_framework.routers import DefaultRouter

from apps.partners.views import PartnerView


router = DefaultRouter()
router.register('partners', PartnerView)

urlpatterns = []
urlpatterns += router.urls
