from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class SnusProdut(models.Model):
    Navn = models.CharField(max_length=100)
    ProdutName = models.CharField(max_length=100)
    nikotinindhold = models.IntegerField()
    Prise = models.FloatField()
    Description = models.TextField()
    img = models.ImageField(upload_to='SnusBildere', default="default")
    valdait = models.IntegerField(default=0)

    def __str__(self):
        return self.ProdutName + " " + self.Navn



class kontakt(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Name