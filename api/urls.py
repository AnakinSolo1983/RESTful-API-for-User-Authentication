from django.urls import path
from .views import RegisterUserAPIView, LogoutView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#from rest_framework.authtoken import views
from .views import CustomTokenObtainpairView, MeView
from django.contrib import admin


#The url paths for user registration, user logout, user authentication, retrieving user details and updating them, and refreshing tokens
#respectively.
urlpatterns = [
  path('api/register/',RegisterUserAPIView.as_view(), name='User-Registration'),
  path('api/logout/', LogoutView.as_view(), name='Logout'),
  path('api/login/', CustomTokenObtainpairView.as_view()),
  path('api/me/', MeView.as_view(), name= 'me'),
  path('api/refresh/', TokenRefreshView.as_view()),
  path('admin/', admin.site.urls)
]
