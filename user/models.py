from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     female = 'F'
#     male = 'M'
#     gender_list = [(female,'female'),(male, 'male')]
#     gender = models.CharField(max_length=10, choices=gender_list, default=female)
#     phone_number = models.CharField(max_length=11, unique=True)

