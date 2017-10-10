from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
