# outstaff/serializers.py
from rest_framework import serializers
from .models import OutstaffCandidate, JobBrief

class JobBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobBrief
        fields = '__all__'

class OutstaffCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutstaffCandidate
        fields = '__all__'
