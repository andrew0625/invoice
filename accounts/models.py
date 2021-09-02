from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
	organization = models.CharField(max_length=256)
	address1 = models.CharField(max_length=256, blank=True)
	address2 = models.CharField(max_length=256, blank=True)
	city = models.CharField(max_length=128, blank=True)
	state = models.CharField(max_length=2, blank=True)
	zip = models.CharField(max_length=12, blank=True)
	phone = models.CharField(max_length=15, blank=True)
	
	def __str__(self):
	  return self.username
	
		
	
 





    

   
