from django.db import models

# Create your models here.
class Status(models.Model):
	status = models.TextField(max_length=160)
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.status

class Comment(models.Model):
	comment = models.TextField(max_length=160)
	created_date = models.DateTimeField(auto_now_add=True)
	status = models.ForeignKey(Status, null=True, blank=True)

	def __str__(self):
		return self.comment