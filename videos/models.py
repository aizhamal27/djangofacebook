from django.db import models
from users.models import User

# Create your models here.
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_video")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    video_file = models.FileField(upload_to="videos/")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class VideoLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="video_user_like")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="user_liked_video")

    def __str__(self):
        return f"{self.user} {self.video}"

class VideoComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="video_comment_user")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comment_video")
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

