from rest_framework.routers import DefaultRouter

from apps.faq.views import FAQView


router = DefaultRouter()
router.register('faq', FAQView)

urlpatterns = [] 

urlpatterns += router.urls
