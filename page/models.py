from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class Carte(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    image = models.ImageField(upload_to='carte/', null=True, blank=True)

    def __str__(self):
        return self.title
