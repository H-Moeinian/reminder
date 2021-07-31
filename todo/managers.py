from datetime import datetime, timezone
from django.db import models
from django.db.models import Count


class ExpiredTasksManager(models.Manager):
    def get_queryset(self):
        return super(ExpiredTasksManager, self).get_queryset().filter(set_to_time__lt=datetime.now(timezone.utc))


class EmptyCategoryManager(models.Manager):
    def get_queryset(self):
        return super(EmptyCategoryManager, self).get_queryset().annotate(num_tasks=Count('tasks')).filter(num_tasks=0)
