from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to = "profile_image/")

    def __str__(self):
        return f"{self.username}"

class UserFollower(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following_user")

    def __str__(self):
        return f"Пользователь {self.from_user} подписан {self.to_user}"