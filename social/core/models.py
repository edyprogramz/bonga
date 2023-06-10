from django.db import models
# from django.contrib.auth.models import User
import uuid
from datetime import datetime
from django.contrib.auth.models import User

# ANOTHER WAY TO GET user
# from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to="profile_images", default="blankImage.jpeg")
    location = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    # profile = models.ForeignKey(Profile, related_name="profile", on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=255)
    image = models.ImageField(upload_to="post_images")
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user