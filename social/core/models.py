from django.db import models
# from django.contrib.auth.models import User

# ANOTHER WAY TO GET user
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to="profile_images", default="blankImage.jpeg")
    location = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.username
    
    