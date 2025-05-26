# outsource/serializers.py
from rest_framework import serializers
from .models import OutsourceRequest, OutsourceStage, OutsourceProgress

class OutsourceStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsourceStage
        fields = '__all__'


class OutsourceRequestSerializer(serializers.ModelSerializer):
    stages = OutsourceStageSerializer(many=True, read_only=True)
    progress_percentage = serializers.DecimalField(
        source='progress.progress_percentage', max_digits=5, decimal_places=2, read_only=True
    )

    class Meta:
        model = OutsourceRequest
        fields = ['id', 'user', 'title', 'nda_link', 'created_at', 'stages', 'progress_percentage']


class OutsourceProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsourceProgress
        fields = '__all__'