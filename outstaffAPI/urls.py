# outstaff/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OutstaffCandidateViewSet, JobBriefViewSet

router = DefaultRouter()
router.register(r'candidates', OutstaffCandidateViewSet, basename='candidate')
router.register(r'job-briefs', JobBriefViewSet, basename='jobbrief')

urlpatterns = [
    path('', include(router.urls)),
]
