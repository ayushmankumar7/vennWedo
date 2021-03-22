from rest_framework.serializers import ModelSerializer
from backend.models import Video, Like


class VideoCreateSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'owner',
            'video_bucket_id',
            'title',
            'description',
            'thumbnail',
        ]


class VideoListSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class VideoUpdateSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'thumbnail',
        ]


class VideoDeleteSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
