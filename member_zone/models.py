from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appareil = models.CharField(max_length=255)
    observations = models.TextField(null=True)

    def __str__(self):
        return self.user