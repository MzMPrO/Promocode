from django.db import models

from apps.user.validators import phone_validator


class Region(models.Model):
    name = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    chat_id = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[phone_validator])
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    balance = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name}'
