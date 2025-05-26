# outsource/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    OutsourceRequestViewSet,
    OutsourceStageViewSet,
    OutsourceProgressViewSet,
)

router = DefaultRouter()
router.register(r'requests', OutsourceRequestViewSet, basename='outsource-request')
router.register(r'stages', OutsourceStageViewSet, basename='outsource-stage')
router.register(r'progress', OutsourceProgressViewSet, basename='outsource-progress')

urlpatterns = [
    path('', include(router.urls)),
]