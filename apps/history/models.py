from django.db import models

from apps.promocode.models import Promocode
from apps.user.models import User


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    promocode = models.ForeignKey(Promocode, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
