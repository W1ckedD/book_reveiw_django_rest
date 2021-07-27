from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import User
from users.serializers import UserSerializer

class RegisterSerializer(serializers.ModelSerializer):
  profile = serializers.PrimaryKeyRelatedField(read_only=True)
  class Meta:
    model = DjangoUser
    fields = ('username', 'email', 'password', 'profile')

  def create(self, validated_data):
    user = DjangoUser.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password']
    )
    return user




class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, attrs):
    user = authenticate(**attrs)
    if user and user.is_active:
      return user
    raise serializers.ValidationError('Invalid credentials')


class RetrieveUserSerializer(serializers.ModelSerializer):
  profile = UserSerializer(User.objects.all(), read_only=True)
  class Meta:
    model = DjangoUser
    fields = ('id', 'username', 'email', 'profile')