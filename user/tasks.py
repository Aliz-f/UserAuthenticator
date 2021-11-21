from celery import shared_task
from .models import UserProfile


@shared_task
def create_spam_user():
    pass