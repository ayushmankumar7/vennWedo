from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class CustomRegisterSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'password')
