from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True)

    mobile_no = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    profilePicture = models.FileField(upload_to='photos/%Y/%m/%d', blank=True)

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