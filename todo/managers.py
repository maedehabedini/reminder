from datetime import datetime, timezone
from django.db import models
from django.db.models import Count


class Due_past_tasks(models.Manager):
    def get_queryset(self):
        return super(Due_past_tasks, self).get_queryset().filter(due_date__lt=datetime.now(timezone.utc))


class Empty_category(models.Manager):
    def get_queryset(self):
        return super(Empty_category, self).get_queryset().annotate(num_tasks=Count('tasks')).filter(num_tasks=0)
