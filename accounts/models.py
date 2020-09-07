from django.db import models
from django.utils import timezone
from django.conf import settings

from django import forms
# Create your models here.


class Profile(models.Model):
    # 유저
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 이름
    name = models.CharField(max_length=10)
    # 닉네임
    nickname = models.CharField(max_length=10, default="")
    # 이미지 주소
    imageURL = models.CharField(max_length=100)
    # 모델 생성 날짜
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
