from django.contrib import admin
from .models import OutstaffCandidate, JobBrief

@admin.register(OutstaffCandidate)
class OutstaffCandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rate', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'role', 'created_at')
    search_fields = ('name', 'role')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('name', 'role', 'rate', 'cv_link', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        # Optionally restrict adding in admin if you only want to allow via the app
        return True

@admin.register(JobBrief)
class JobBriefAdmin(admin.ModelAdmin):
    list_display = ('title', 'brief_link', 'description', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)