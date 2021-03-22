from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Video(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    video_bucket_id = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    thumbnail = models.ImageField(null=True)
    publishing_date = models.DateTimeField(default=timezone.now, blank=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = {
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
}


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.video)
