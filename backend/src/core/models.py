from django.db import models
import time
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings

# Create your models here.


def avatar_upload_path(instance, filename):
    """This function will return the upload path for avatar"""
    return '/'.join(["avatar",str(instance.id),filename])

class UserManager(BaseUserManager):
    """
    Custom User Manager Class
    """
    def create_user(self, email, password=None, **extra_fields):
        """Create and Saves user"""
        if not email:
            email = str(time.time())+"@libtech.in"
          #  raise ValueError("Users must have an email address")
            
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    user_role = models.CharField(max_length=20, blank=True, null=True,
                                 default='client')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_user_manager = models.BooleanField(default=False)
    login_attempt_count = models.PositiveSmallIntegerField(default=0)
    is_locked = models.BooleanField(default=False)
    avatar = models.ImageField(blank=True, null=True,
                               upload_to=avatar_upload_path)
    avatar_url = models.URLField(max_length=1024, null=True, blank=True)
    provider = models.CharField(max_length=32, default="native")
    phone = models.CharField(max_length=32)
    objects = UserManager()
    USERNAME_FIELD = 'email'


