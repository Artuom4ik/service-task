from django.db import models
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Ожидает исполнителя'),
        ('in_progress', 'В процессе'),
        ('completed', 'Выполнена'),
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата обновления"
    )
    closed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата закрытия"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Статус"
    )
    report = models.TextField(blank=True, verbose_name="Отчёт")

    def __str__(self):
        return f'Task {self.id} - {self.status}'
