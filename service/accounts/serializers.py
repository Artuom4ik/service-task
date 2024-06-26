from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
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
            'email': {'required': True},
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'role': {'required': True},
            'phone_number': {'required': True},
            'middle_name': {'required': False},
        }

    def validate_role(self, value):
        if self.instance and self.instance.role != value:
            raise serializers.ValidationError("You cannot change the user role")

        return value

    def create(self, validated_data):
        user = Users.objects.create_user(
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

        token['username'] = user.username
        token['password'] = user.password

        return token
