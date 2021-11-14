from django.urls import path
from .views import register_user, login_user

urlpatterns = [
   path('register/', register_user.as_view()),
   path('login/', login_user.as_view()),
]
