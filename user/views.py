from django.db.models import query
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.views.generic.base import RedirectView
from rest_framework import generics, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, loginSerializer


# Create your views here.
class register_user (generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class login_user(generics.GenericAPIView):
    serializer_class = loginSerializer
    queryset = User.objects.all()

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user= authenticate(username = username, password = password)
        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class view_user(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    authentication_classes = [SessionAuthentication, BasicAuthentication] #***For Authentication -> first session auth, second basic auth
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)



class logout_user(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    authentication_classes = [SessionAuthentication, BasicAuthentication] #***For Authentication -> first session auth, second basic auth
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/admin/login/?next=/admin/')