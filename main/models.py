from django.db import models

# Create your models here.
class user(models.Model):
	firstname=models.TextField()
	lastname=models.TextField()
	username=models.CharField(max_length=15)
	password=models.TextField()

	def __str__(self):
		return self.username

class post(models.Model):
	post_id=models.AutoField(primary_key=True)
	content=models.TextField()
	created_by=models.TextField()
	created_on=models.DateField()
	created_at=models.TimeField()
	likes=models.IntegerField()
	dislikes=models.IntegerField()

	def __str__(self):
		return self.created_by