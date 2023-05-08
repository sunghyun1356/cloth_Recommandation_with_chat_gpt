from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Information(models.Model):
    image = models.ImageField(verbose_name = '이미지', null=True, blank=True)
    content = models.TextField(verbose_name='내용')
