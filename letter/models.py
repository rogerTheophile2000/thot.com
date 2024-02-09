from django.utils import timezone
from django.db import models

# Create your models here.
class Header(models.Model):
    logo = models.ImageField()
    description = models.TextField()

class Footer(models.Model):
    description = models.TextField()
    detail = models.TextField()

class Letter(models.Model):
    object = models.TextField()
    header = models.ForeignKey(Header, on_delete=models.CASCADE)
    introduction = models.TextField()
    developpement = models.TextField()
    conclusion = models.TextField()
    dataEmission = models.DateTimeField(default=timezone.now)
    destinateur = models.CharField(max_length= 150)
    expediteur = models.CharField(max_length= 150)
    copieConforme = models.TextField()
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE)
    
    
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)