from django.db import models

class Feed(models.Model):
    name = models.CharField(max_length=255)
    userImage = models.ImageField(upload_to='uploads/')
    postImage = models.ImageField(upload_to='uploads/')
    likes = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    liked = models.BooleanField(default=False)
    content = models.TextField(max_length=255)
    filter = models.CharField(max_length=255, blank=True, null=True)