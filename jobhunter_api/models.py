from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name,location_preference,skills, experience, resume, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,location_preference= location_preference, skills=skills, experience=experience, resume=resume,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    location_preference = models.CharField(max_length=255,default='')
    skills = models.CharField(max_length=255,default='')
    experience = models.FloatField(default=0)
    resume = models.URLField(max_length=255,default='')
    
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    def __str__(self):
        """Return string representation of user"""
        return self.email


class Openings(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    expired_on = models.DateTimeField()
    image = models.URLField(max_length=255,default='')
    experience = models.FloatField(default=0)
    skills = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    contact_mail = models.EmailField(max_length=255)
    location = models.CharField(max_length=50)
    website = models.URLField(max_length=255,default='')
    company = models.CharField(max_length=255)
    company_logo = models.URLField(max_length=255)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text


