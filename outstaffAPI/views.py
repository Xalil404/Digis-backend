from django.shortcuts import render

# outstaff/views.py
from rest_framework import viewsets
from .models import OutstaffCandidate, JobBrief
from .serializers import OutstaffCandidateSerializer, JobBriefSerializer

class JobBriefViewSet(viewsets.ModelViewSet):
    queryset = JobBrief.objects.all()
    serializer_class = JobBriefSerializer

class OutstaffCandidateViewSet(viewsets.ModelViewSet):
    queryset = OutstaffCandidate.objects.all()
    serializer_class = OutstaffCandidateSerializer
