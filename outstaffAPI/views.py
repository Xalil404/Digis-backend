from django.shortcuts import render

# outstaff/views.py
from rest_framework import viewsets, permissions
from .models import OutstaffCandidate, JobBrief
from .serializers import OutstaffCandidateSerializer, JobBriefSerializer

class JobBriefViewSet(viewsets.ModelViewSet):
    serializer_class = JobBriefSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JobBrief.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OutstaffCandidateViewSet(viewsets.ModelViewSet):
    serializer_class = OutstaffCandidateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return OutstaffCandidate.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
