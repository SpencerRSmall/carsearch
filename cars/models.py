from django.db import models

class Car(models.Model):
    make = models.TextField()
    year = models.IntegerField()
    model = models.TextField()
    mpg = models.IntegerField()

