from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .abstract_base_model import BaseModel


class UserManager(BaseUserManager):

    def create_user(self, email, password, username, **extra_fields):

        if not email:
            raise ValueError('user must have na email')
        if not username:
            raise ValueError('user must have a username')

        user_email = self.normalize_email(email)
        user = self.model(username=username, email=user_email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, username, **extra_fields):

        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True')
        if extra_fields.get('is_verified') is not True:
            raise ValueError('Superuser must have is_verified=True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True')

        user = self.create_user(email, username, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    about = models.TextField()
    image = models.ImageField()
    github = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField()
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.email
