from rest_framework.routers import DefaultRouter
from .views import StageViewSet

router = DefaultRouter()

router.register(
    "",
    StageViewSet,
    basename="stages"
)

urlpatterns = router.urls