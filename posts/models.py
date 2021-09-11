
from django.db import models


class Math(models.Model):
    operation = models.CharField(max_length = 6)
    a = models.IntegerField()
    b = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"id:{self.id}, a={self.a}, b={self.b}, op={self.operation}"

class Result(models.Model):
    value = models.FloatField(blank=True, null=True, unique=True)
    error = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True
    )

    def __str__(self):
        return f"value: {self.value} | error: {self.error}"