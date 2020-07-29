from django.db import models
from django.utils import timezone

# Create your models here.


class Director(models.Model):
    # 이름
    name = models.CharField(max_length=10)
    # 이미지 주소
    imageURL = models.CharField(max_length=100)
    # 모델 생성 날짜
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
