from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'middle_name',
            'phone_number',
            'role'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data.get('middle_name', ''),
            phone_number=validated_data.get('phone_number', ''),
            role=validated_data['role']
        )

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role

        return token
