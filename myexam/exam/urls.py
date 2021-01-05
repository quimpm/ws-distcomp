from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ExamViewSet

router = SimpleRouter()
router.register("", ExamViewSet)

urlpatterns = router.urls
