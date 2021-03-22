from django.urls import path
from backend.views import (
    VideoCreateApi,
    VideoListApi,
    VideoUpdateApi,
    VideoDeleteApi,
)


urlpatterns = [
    path('video/list/', VideoListApi.as_view()),
    path('video/create/', VideoCreateApi.as_view()),
    path('video/update/<int:pk>', VideoUpdateApi.as_view()),
    path('video/delete/<int:pk>', VideoDeleteApi.as_view())
]
