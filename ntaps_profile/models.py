from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    expertise = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    email = models.EmailField()
