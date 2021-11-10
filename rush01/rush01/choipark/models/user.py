from django.db import models
from django.conf import settings

class UserProfileModel(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('name', max_length=30)
    surname = models.CharField('surname', max_length=30)
    email = models.EmailField('email', blank=True)
    description = models.TextField('description', blank=True)
    profile_image = models.ImageField('profile_image', blank=True, null=True, upload_to='image')
