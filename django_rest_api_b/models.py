from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    '''Manager for user profile'''
    def create_user(self, email, name, password=None):
        '''Create a new user profile'''
        if not email:
            raise ValueError('User must have an email address')
        #convert 2nd half email addresss to all lower case and make it case insensitive
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        #encrypt password as a hash
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        '''Create and save a new superuser with given details'''
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionMixin):
    """Database model for users in the system"""
    #create email column in UserProfile database table, with EmailField, max_length-255, field must be unique
    email = models.EmailField(max_length=255, unique=True)
    #creat name column in UserProfile database table
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    #PermissionMixin creates is_superuser, we need to define is_staff
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    #overwrite username field with email field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Method to retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Method to retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email

