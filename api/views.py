from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, View
from rest_framework.response import Response
from .serializers import RegisterSerializer, LogoutSerializer, UserSerializer
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import serializers, views, response, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken, Token, AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
#from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
#from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import views, viewsets, status
import uuid
from rest_framework import authentication, permissions
from django.views.generic import DetailView

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
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication as jwt

from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

#Class based view to register user:
class RegisterUserAPIView(generics.CreateAPIView):

  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer



from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication




from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import uuid

from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#Class view to obten access and refresh tokens:
class CustomTokenObtainpairView(TokenObtainPairView):
    
    serializer_class = CustomTokenObtainPairSerializer

from rest_framework import viewsets
from rest_framework import generics
#from django.views.generic.list import ListView
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

#Class view to logout the user:
class LogoutView(generics.GenericAPIView):
    
    #generics.GenericAPIView
    serializer_class = LogoutSerializer
    permission_classes = (AllowAny,)
    #permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (permissions.AllowAny)

    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "User logged out."}, status=status.HTTP_200_OK)


from rest_framework.response import Response
from .serializers import UserSerializer #Importing UserSerializer.

#Class view to retrive user information and update it:
class MeView(APIView):
    
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)#"""

    def put(self, request):
        
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
        
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
