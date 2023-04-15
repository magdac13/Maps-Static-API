from django.db import models


# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    geo_lat = models.FloatField()
    geo_long = models.FloatField()

