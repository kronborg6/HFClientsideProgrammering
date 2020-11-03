from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Produt(models.Model):
    Name = models.CharField(max_length=100)
    ProductName = models.CharField(max_length=100)
    NicotineContent = models.IntegerField()
    Price = models.FloatField()
    Description = models.TextField()
    Img = models.ImageField(upload_to='SnusBildere', default='default.png')
    Value = models.BooleanField(default=False)

    def __str__(self):
        return self.ProductName + " " + self.Name

    def FullName(self):
        return self.ProductName + " " + self.Name

    def save(self):
        super().save()

        img = Image.open(self.Img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.Img.path)


class kontakt(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Name