# outsource/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OutsourceStage, OutsourceProgress

def calculate_progress(outsource_request):
    total = outsource_request.stages.count()
    if total == 0:
        return 0.0
    completed = outsource_request.stages.filter(completed=True).count()
    return round((completed / total) * 100, 2)


@receiver([post_save, post_delete], sender=OutsourceStage)
def update_outsource_progress(sender, instance, **kwargs):
    try:
        progress = instance.outsource_request.progress
        progress.progress_percentage = calculate_progress(instance.outsource_request)
        progress.save()
    except OutsourceProgress.DoesNotExist:
        pass