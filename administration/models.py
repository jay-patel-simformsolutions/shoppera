from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import MaxLengthValidator, MinLengthValidator


def phone_validator(value):
	if len(str(value)) == 10:
		pass
	else:
		raise ValidationError('Phone Number sholud be of 10 digits')


class UserProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.BigIntegerField(validators=[phone_validator])

	def __str__(self):
		return self.user.username

	class Meta:
		db_table = 'user_profile'
