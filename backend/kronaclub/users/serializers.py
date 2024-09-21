from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import (
    CustomUser,
    TypeOfUser,
    UserType
)


class TypeOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfUser
        fields = '__all__'


class UserTypeSerializer(serializers.ModelSerializer):
    type_id = serializers.CharField(source='type_of_user.id', read_only=True)
    type_name = serializers.CharField(source='type_of_user.name', read_only=True)
    class Meta:
        model = UserType
        fields = ('type_id', 'type_name')


class CustomUserSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'date_of_birth', 'telegram_login', 'telegram_id', 'phone_number', 'user_type')
        read_only_fields = ('email', 'user_type')


class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'date_of_birth', 'password')
