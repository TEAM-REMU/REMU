from django.db import models
from django.utils import timezone

class Production(models.Model):
    # 이름
    name = models.CharField(max_length=10)
    # sns 주소
    sns_link = models.TextField()
    # 이미지 주소
    image_url = models.CharField(max_length=100)
    # 모델 생성 날짜
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + '('+str(self.pk)+')'


class Director(models.Model):
    # 이름
    name = models.CharField(max_length=10)
    # 프로덕션
    production = models.ForeignKey(Production, on_delete=models.CASCADE, blank=True, null=True)
    # sns 주소
    sns_link = models.TextField()
    # 이미지 주소
    image_url = models.CharField(max_length=100)
    # 모델 생성 날짜
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + '('+str(self.pk)+')'

