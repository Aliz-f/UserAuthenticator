from rest_framework import generics, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from django.contrib.auth.models import User
from .serializers import UserProfileSerializer


# Create your views here.
class register_user (generics.GenericAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
