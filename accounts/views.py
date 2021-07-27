from django.contrib import auth
from django.contrib.auth.models import User as DjangoUser
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework import permissions
from knox.models import AuthToken
from .serializers import LoginSerializer, RegisterSerializer, RetrieveUserSerializer
from users.models import User
from users.serializers import UserSerializer


class RegisterAPIView(GenericAPIView):
  serializer_class = RegisterSerializer
  def post(self, request, *args, **kwargs):
    try:
      django_user_serializer = self.get_serializer(data=request.data)
      django_user_serializer.is_valid(raise_exception=True)
      django_user = django_user_serializer.save()
      user = UserSerializer(data={
        'first_name': request.data['first_name'],
        'middle_name': request.data['middle_name'],
        'last_name': request.data['last_name'],
        'user': django_user.id,
      })
      user.user = django_user
      user.is_valid(raise_exception=True)
      user.save()
      _, token = AuthToken.objects.create(django_user)

      return Response({
        'token': token,
        'user': RetrieveUserSerializer(django_user).data,
      })
    except NameError as err:
      print(err)



class LoginAPIView(GenericAPIView):
  serializer_class = LoginSerializer
  
  def post(self, request, *args, **kwargs):
    try:
      django_user_serializer = self.get_serializer(data=request.data)
      django_user_serializer.is_valid(raise_exception=True)
      django_user = django_user_serializer.validated_data
      _, token = AuthToken.objects.create(django_user)

      return Response({
        'token': token,
        'user': RetrieveUserSerializer(django_user).data,
      })
    except NameError as err:
      print(err)

class RetrieveUserAPIView(RetrieveAPIView):
  serializer_class = RetrieveUserSerializer

  permission_classes = [
    permissions.IsAuthenticated
  ]

  def get_object(self):
    return self.request.user

