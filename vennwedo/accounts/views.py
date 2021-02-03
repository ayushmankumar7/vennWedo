from django.contrib.auth import get_user_model
from accounts.serializers import CustomRegisterSerializer
from rest_framework import permissions
from rest_framework import generics


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomRegisterSerializer
