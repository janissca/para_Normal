from django.db import models
from django.conf import settings
from eventsapp.models import Event


class ScheduledTask(models.Model):
    STATUS_CHOICES = (
        ('pending', 'В ожидании'),
        ('processing', 'Выполняется'),
        ('completed', 'Завершено'),
        ('failed', 'Провалено'),
        ('cancelled', 'Отменено'),
    )

    celery_id = models.CharField(verbose_name='ID задачи в Celery', max_length=255)
    start_date = models.DateTimeField(verbose_name='Дата и время начала задачи', auto_now_add=True)
    created_date = models.DateTimeField(verbose_name='Дата и время создания задачи', auto_now_add=True)
    status = models.CharField(verbose_name='Статус задачи', choices=STATUS_CHOICES, max_length=20, default='pending')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='task')
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='task')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self) -> str:
        return  self.celery_id
