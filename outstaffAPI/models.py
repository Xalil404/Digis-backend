# outstaff/models.py
from django.db import models

class JobBrief(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brief_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OutstaffCandidate(models.Model):
    class Status(models.TextChoices):
        NOT_AVAILABLE = 'not_available', 'Not Available'
        AVAILABLE = 'available', 'Available'
        INTERVIEW = 'interview', 'Interview'
        TEST_TASK = 'test_task', 'Test Task'
        APPROVED = 'approved', 'Approved'

    name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    role = models.CharField(max_length=100)
    cv_link = models.URLField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.name} - {self.role}"
