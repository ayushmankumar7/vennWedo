from rest_framework import generics
from backend.serializer import (
    VideoCreateSerializer,
    VideoListSerializer,
    VideoUpdateSerializer,
    VideoDeleteSerializer
)
from backend.models import Video
from rest_framework.permissions import IsAuthenticated

class VideoCreateApi(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoCreateSerializer


class VideoListApi(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoListSerializer


class VideoUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoListSerializer


class VideoDeleteApi(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoDeleteSerializer
