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
    type = serializers.CharField(source='type_of_user.name')
    class Meta:
        model = UserType
        fields = ('id', 'type')


class CustomUserSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'date_of_birth', 'telegram_login', 'telegram_id', 'phone_number', 'user_type')
        read_only_fields = ('email', 'user_type')

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
    #     instance.telegram_login = validated_data.get('telegram_login', instance.telegram_login)
    #     instance.telegram_id = validated_data.get('telegram_id', instance.telegram_id)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #     instance.save()

    #     return instance

class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'date_of_birth', 'password')
