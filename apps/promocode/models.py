from django.db import models


class Promocode(models.Model):
    promocode = models.CharField(max_length=255, unique=True)
    price = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.promocode}"
