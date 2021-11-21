from celery import shared_task
from .models import UserProfile
from django.contrib.auth.models import User
import string
import random

String_length = 15


@shared_task
def create_spam_user():
    randomUsername = ''.join(random.choices(string.ascii_uppercase + string.digits, k = String_length))
    randomPassword = ''.join(random.choices(string.ascii_uppercase + string.digits, k = String_length))
    randomEmail = ''.join(random.choices(string.ascii_uppercase + string.digits, k = String_length))+'@gmail.com'
    randomPhoneNumber = ''
    for i in range(0,11):
        randomPhoneNumber += str(random.randint(0,9))
    user = User.objects.create_user(username=randomUsername, password=randomPassword, email=randomEmail)
    userprofile = UserProfile.objects.create(user = user, phone_number = randomPhoneNumber, gender='M')