from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomRegisterSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        user = User.objects.create_user(name=validated_data['name'], username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=make_password(
                                            validated_data['password']),
                                        )
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'password')
        read_only_fields = ('email',)
