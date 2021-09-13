from django.shortcuts import reverse
from .managers import *
from django.db import models

PRIORITIES = (
    ('adanger', 'Priority High'),
    ('bwarning', 'Priority Medium'),
    ('csuccess', 'Priority Low')
)


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    empty_category = Empty_category()
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('category_tasks', args=[str(self.id)])

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='tasks', null=True, blank=True)
    is_done = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    objects = models.Manager()
    due_past_manager = Due_past_tasks()
    priority = models.CharField(
        max_length=30,
        choices=PRIORITIES,
        default=PRIORITIES[0][0]
    )
    complete = models.IntegerField(default=0)

    class Meta:
        ordering = ["-date_of_creation"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

