from django.db import models
import uuid
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class User(models.Model):
    
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=100)

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

