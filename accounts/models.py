from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length = 50)
	short_bio = models.CharField(max_length= 99999, validators=[MinLengthValidator(255, message= "Bio has to be more than 255 characters!")]) #https://stackoverflow.com/questions/2470760/charfield-with-fixed-length-how


# Create your models here.
