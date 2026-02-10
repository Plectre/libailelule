from django.db import models
from django.contrib.auth.models import User

class Logs(models.Model):
    appareil = models.CharField(max_length=128)
    depart = models.DateField()
    retour = models.DateField()
    observations = models.TextField(null=True, blank=True)
    pilot = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pilot.username