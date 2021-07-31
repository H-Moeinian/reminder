from django.db import models
from django.db.models import Count
from django.urls import reverse
from datetime import datetime, timezone
from .managers import *


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100)
    objects = models.Manager()
    emptyCategory = EmptyCategoryManager()

    def get_absolute_url(self):
        return reverse('category_tasks', args=[str(self.id)])


class Task(models.Model):
    PRIORITY_CHOICES = [('1', 'not important'), ('2', 'important'), ('3', 'very important'), ('4', 'necessary')]
    CATEGORY_CHOICES = [('in', 'incidental'), ('ro', 'routine'), ('pj', 'project'), ('pr', 'problem')]
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='tasks')
    priority = models.CharField(choices=PRIORITY_CHOICES, default='2', max_length=1)
    set_to_time = models.DateTimeField()
    done = models.BooleanField(default=False)
    objects = models.Manager()
    expiredTasks = ExpiredTasksManager()

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])


