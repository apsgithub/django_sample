from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=255, unique=True)
    lname = models.CharField(max_length=255, unique = False)
    email = models.EmailField(max_length=264,unique=True)


