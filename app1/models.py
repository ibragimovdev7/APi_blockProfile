from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Profile(models.Model):
    fullname = models.CharField(max_length=100)
    image = models.ImageField()
    phone_number = models.CharField(max_length=20)
    description = RichTextField()

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            ''

    def __str__(self):
        return self.fullname