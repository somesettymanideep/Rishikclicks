from django.db import models
from datetime import datetime


# Create your models here.
class Bannersection(models.Model):
    Id = models.AutoField(primary_key=True)
    Title =  models.CharField(max_length=225,default="title")
    Bannerimg = models.ImageField(upload_to='uploads/')
    CreatedName =  models.CharField(max_length=100)
    Create_at = models.DateTimeField(default=datetime.now)
    

    class Meta:
        ordering = ['-Create_at']

    def __str__(self):
            return self.Title