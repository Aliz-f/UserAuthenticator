from rest_framework import fields, serializers
from .models import UserProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
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

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileSerializer (serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields ='__all__'

    def create(self, validated_data):
        username = validated_data.pop('user')
        myUser = User.objects.create_user(**username)
        return UserProfile.objects.create(user = myUser, **validated_data)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number', '')
        if UserProfile.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'Phone_number':('Phone number is already in use')})
        return super().validate(attrs)

 