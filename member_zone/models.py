from django.db import models
from django.contrib.auth.models import User



""" class Log(models.Model):
    appareil = models.CharField(max_length=255)
    depart = models.CharField(max_length=255)
    retour = models.CharField(max_length=255)
    observations = models.TextField(null=True)
    pilot = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.appareil """
    
class Logs(models.Model):
    appareil = models.CharField(max_length=255)
    depart = models.DateField()
    retour = models.DateField()
    observations = models.TextField(null=True, blank=True)
    pilot = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.appareil