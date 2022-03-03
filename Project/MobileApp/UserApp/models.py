from pickle import FALSE, TRUE
from django.db import models

class Location(models.Models):
    latitude = models.FloatField()
    longitude = models.FloatField()

class User(models.Model):
        userID = models.BigIntegerField()
        email = models.EmailField()
        name = models.CharField(max_length=50)
        password = models.CharField(max_length=50)
        gender = models.BinaryField(default=TRUE)
        age = models.PositiveIntegerField()
        hasbicycle = models.BinaryField(default=FALSE)
        currentLocation = Location()
        profilePhoto = models.ImageField(upload_to="pictures")
        socialAccount = models.CharField(max_length=50)
