from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Task


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        return token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class TaskSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M',
        read_only=True
    )
    updated_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M',
        read_only=True
    )
    deadline = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {'drafter': {'read_only': True}}
