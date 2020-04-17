from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin


class UserProfile(AbstractBaseUser, PermissionMixin):
    """Database model for users in the system"""
    #create email column in UserProfile database table, with EmailField, max_length-255, field must be unique
    email = models.EmailField(max_length=255, unique=True)
    #creat name column in UserProfile database table
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
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