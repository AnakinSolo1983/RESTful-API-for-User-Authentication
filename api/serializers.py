from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import serializers, views, response, status, permissions

import uuid
import jwt
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from django.db import models
from django.utils import timezone
from rest_framework import serializers, status, views, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ["id", "username", "email"]

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True, validators=[validate_password])
  class Meta:
    model = User
    fields = ('id', 'password', 'email')

  def create(self, validated_data):

    user = User.objects.create(
      #id=validated_data['id'],
      email=validated_data['email'],
      username=validated_data['email'],
      password=validated_data['password']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user

from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#Serializer to get Access and Refresh Tokens.
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        
        token = super().get_token(user)
        token['name'] = user.username
        # you can put any other fields you wish and within the user object

        return token

#Serializer to Logout User.
class LogoutSerializer(serializers.Serializer):
  
  refresh = serializers.CharField()
  def validate(self, attrs):
    
    self.refresh_token = attrs.get('refresh_token')
    return attrs

  def save(self, **kwargs):
    
    try:
       
       RefreshToken(self.refresh_token).blacklist()

    except TokenError:
       
       self.fail('Invalid token.')
    #pass#"""
