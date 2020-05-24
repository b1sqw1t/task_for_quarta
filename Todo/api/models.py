from django.db import models

# Create your models here.

class TodoModel(models.Model):

    todo = models.CharField(max_length=1024, verbose_name='Описание задачи')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    changed = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата изменения')
    expiry_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания задачи')
    status = models.BooleanField(default=False)
    completion_date = models.DateTimeField(verbose_name='дата выполнения')