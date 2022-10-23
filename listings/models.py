from django.db import models

class Listing(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    brand = models.CharField(max_length=150)
    used = models.IntegerField()
    price = models.IntegerField()

