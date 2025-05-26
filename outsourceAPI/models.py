from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class OutsourceRequest(models.Model):
    """
    Represents an outsource project request from a client.
    Includes an NDA link and is tied to a user/client.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outsource_requests')
    title = models.CharField(max_length=255)
    nda_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OutsourceStage(models.Model):
    """
    Represents a section of the outsource request pie chart,
    with a document link and completion status.
    """
    class StageType(models.TextChoices):
        BUSINESS_REQUIREMENTS = 'business_requirements', 'Business Requirements'
        PROJECT_DOCUMENTATION = 'project_documentation', 'Project Documentation'
        TECHNICAL_QUESTIONS = 'technical_questions', 'Technical Questions'
        ANALYSIS = 'analysis', 'Analysis'
        RECOMMENDED_TECH_STACK = 'recommended_tech_stack', 'Recommended Tech Stack'
        ESTIMATION = 'estimation', 'Estimation'
        PROPOSAL = 'proposal', 'Proposal'
        CONTRACT = 'contract', 'Contract'

    outsource_request = models.ForeignKey(OutsourceRequest, on_delete=models.CASCADE, related_name='stages')
    stage_type = models.CharField(max_length=50, choices=StageType.choices)
    document_link = models.URLField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('outsource_request', 'stage_type')  # Prevent duplicate stages per request

    def __str__(self):
        return f"{self.outsource_request.title} - {self.get_stage_type_display()}"


class OutsourceProgress(models.Model):
    """
    Stores the progress percentage of each outsource request for filtering and reporting.
    """
    outsource_request = models.OneToOneField(
        OutsourceRequest,
        on_delete=models.CASCADE,
        related_name='progress'
    )
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.outsource_request.title} - {self.progress_percentage}%"

