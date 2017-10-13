from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=30, default='Unknown')
    birthday = models.CharField(max_length=30, default='Unknown')
    gender = models.CharField(max_length=30, default = 'Unknown')
    expertise = models.CharField(max_length=140, default='null')
    description = models.CharField(max_length=140, default='Unknown')
    email = models.EmailField(default='Unknown')
