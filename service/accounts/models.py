from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Users(User):
    ROLE = {
        ("employee", "Сотрудник"),
        ("client", "Заказчик")
    }
    middle_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Отчество"
    )
    phone_number = PhoneNumberField(
        blank=True,
        region="BY",
        verbose_name="Номер телефона"
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE,
        verbose_name="Роль"
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.role}'
