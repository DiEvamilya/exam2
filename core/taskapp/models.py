from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    class META:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.name

class Tasks(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    end_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey('Category', default='general', on_delete=models.PROTECT)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title