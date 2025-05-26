# outsource/views.py
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import OutsourceRequest, OutsourceStage, OutsourceProgress
from .serializers import (
    OutsourceRequestSerializer,
    OutsourceStageSerializer,
    OutsourceProgressSerializer,
)

class OutsourceRequestViewSet(viewsets.ModelViewSet):
    queryset = OutsourceRequest.objects.all()
    serializer_class = OutsourceRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        OutsourceProgress.objects.create(outsource_request=instance)


class OutsourceStageViewSet(viewsets.ModelViewSet):
    queryset = OutsourceStage.objects.all()
    serializer_class = OutsourceStageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(outsource_request__user=self.request.user)


class OutsourceProgressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OutsourceProgress.objects.all()
    serializer_class = OutsourceProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(outsource_request__user=self.request.user)
