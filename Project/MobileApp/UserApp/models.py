from pickle import FALSE, TRUE
from django.db import models
class User(models.Model):
          email = models.EmailField()
          age = models.PositiveIntegerField()
          gender = models.BinaryField(default=TRUE)
          password = models.CharField(max_length=50)
          hasbicycle = models.BinaryField(default=FALSE)     

#         name = models.CharField(max_length=50)
#         currentLocation = Location()
#         profilePhoto = models.ImageField(upload_to="pictures")
#         socialAccount = models.CharField(max_length=50)
