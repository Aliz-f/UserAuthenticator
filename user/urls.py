from django.urls import path
from .views import register_user, login_user, view_user, logout_user

urlpatterns = [
   path('register/', register_user.as_view()),
   path('login/', login_user.as_view()),
   path('', view_user.as_view()),
   path('logout/',logout_user.as_view()),
]
