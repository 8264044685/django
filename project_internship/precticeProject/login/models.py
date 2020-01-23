from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
# from .validation import validate_file_extension
from django.forms import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator




class userProfile(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True)

    mobile_no = models.BigIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])

    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    profilePicture = models.ImageField(upload_to='photos/%Y/%m/%d')

    def clean_profilePicture(self):
        image_file = self.cleaned_data.get('profilePicture')
        if not image_file.name.endswith(".jpg",".jpeg",".png"):
            raise ValidationError("Only .jpg, .jpeg, .png image accepted")
        return image_file

    def __str__(self):
        return self.user.username

    
# class State(models.Model):
#     state_name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.state_name
#
#
# class Districts(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     dist_name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.dist_name
#
#
# class City(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     dist = models.ForeignKey(Districts, on_delete=models.CASCADE)
#     city_name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.city_name