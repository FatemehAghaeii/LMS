from rest_framework.routers import DefaultRouter

from .views import (
    AttributeViewSet,
    AttributeValueViewSet
)

router = DefaultRouter()

router.register(
    "attributes",
    AttributeViewSet
)

router.register(
    "values",
    AttributeValueViewSet
)

urlpatterns = router.urls