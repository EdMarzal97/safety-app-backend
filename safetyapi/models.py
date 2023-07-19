from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200)
    rate = models.CharField(max_length=20)
    overall = models.CharField(max_length=200)
    transport = models.CharField(max_length=200)
    pickpockets = models.CharField(max_length=200)
    natural = models.CharField(max_length=200)
    mugging = models.CharField(max_length=200)
    terrorism = models.CharField(max_length=200)
    scams = models.CharField(max_length=200)
    women = models.CharField(max_length=200)
    