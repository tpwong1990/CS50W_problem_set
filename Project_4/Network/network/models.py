from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    content = models.CharField(max_length=1000)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "post")
    time = models.DateTimeField(auto_now_add=True)
    like_no = models.PositiveIntegerField(default=0)
    liked_user = models.ManyToManyField(User, blank=True, related_name = "liked_post")

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "writer": self.writer.id,
            "time": self.time,
            "like_no": self.like_no,
        }

class Follow(models.Model):
    to_follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "follower")
    be_followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "followed")
