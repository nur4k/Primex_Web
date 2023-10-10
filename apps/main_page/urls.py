from rest_framework.routers import DefaultRouter

from apps.main_page.views import Main_PageView


router = DefaultRouter()
router.register('main_page', Main_PageView)

urlpatterns = []
urlpatterns += router.urls