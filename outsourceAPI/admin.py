# outsource/admin.py
from django.contrib import admin
from .models import OutsourceRequest, OutsourceStage, OutsourceProgress

@admin.register(OutsourceRequest)
class OutsourceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at')
    search_fields = ('title', 'user__email')


@admin.register(OutsourceStage)
class OutsourceStageAdmin(admin.ModelAdmin):
    list_display = ('id', 'outsource_request', 'stage_type', 'completed', 'updated_at')
    list_filter = ('completed', 'stage_type')
    search_fields = ('outsource_request__title',)


@admin.register(OutsourceProgress)
class OutsourceProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'outsource_request', 'progress_percentage')
    search_fields = ('outsource_request__title',)