# Import restframework
from rest_framework import generics
from rest_framework import status
# from rest_framework import Response
from rest_framework import viewsets


# Import Users App
from apps.users.models import User
from apps.users.api.serializers.user_serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.filter(is_active = True)

  # def get_queryset():
