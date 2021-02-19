from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user= models.OneToOneField(User, on_delete=models.CASCADE)
	hospital=models.CharField(max_length=50,default="none")
 
	def __str__(self):
		return f'{self.user.username} Profile'