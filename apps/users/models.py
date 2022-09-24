from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
from django.contrib.auth.validators import UnicodeUsernameValidator
from .manager import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=150, validators=[UnicodeUsernameValidator], unique=True)
  email = models.EmailField('Correo Electronico', max_length=150, unique=True)
  phoneArea = models.CharField(max_length=15, null=True, blank=True)
  phone = models.CharField(max_length=15, null=True, blank=True, unique=True)
  name = models.CharField(max_length=150, blank=True, null=True)
  last_name = models.CharField(max_length=150, blank=True, null=True)

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  historical = HistoricalRecords()

  objects = UserManager()

  class Meta:
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email', 'name', 'last_name', 'phone']

  def natural_key(self):
    return self.username

  def __str__(self):
    return f'{self.name} {self.last_name}'