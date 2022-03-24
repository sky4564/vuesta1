from django.db import models
from PIL import Image

class Feed(models.Model):
    name = models.CharField(max_length=255)
    userImage = models.ImageField(upload_to='uploads/', blank=True, null=True)
    postImage = models.ImageField(upload_to='uploads/', blank=True, null=True)
    likes = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    liked = models.BooleanField(default=False)
    content = models.TextField(max_length=255)
    filter = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('-date',)

    def get_userImage(self):
        if self.userImage:
            return 'http://127.0.0.1:8000' + self.userImage.url
        return ''

    def get_postImage(self):
        if self.postImage:
            return 'http://127.0.0.1:8000' + self.postImage.url
        return ''

