from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'post_image/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Пользователь {self.user} {self.title}"

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like")

class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        ordering = ("-created",) 