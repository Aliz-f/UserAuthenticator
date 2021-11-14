from enum import unique
from rest_framework import fields, serializers
# from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email':('Email is already in use')})
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError({'username':('Username is already in use')})
        return super().validate(attrs)




