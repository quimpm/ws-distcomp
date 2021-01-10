from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import GradeViewSet

router = SimpleRouter()
router.register("", GradeViewSet)

urlpatterns = router.urls