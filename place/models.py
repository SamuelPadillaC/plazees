from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    def __str__(self):
        return self.name

class Point(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=25)
    longitude = models.FloatField(max_length=25)
    def __str__(self):
        return "Point: " + str(self.id)