from django.db import models
from django.utils import timezone
from django.conf import settings
from director.models import Director, Production
# Create your models here.


class MusicVideo(models.Model):
    # 제목
    title = models.CharField(max_length=50)
    # 감독
    director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=True, null=True)
    # 프로덕션
    production = models.ForeignKey(Production, on_delete=models.CASCADE, blank=True, null=True)
    # 비디오 주소
    video_link = models.CharField(max_length=50)
    # 아티스트
    artist = models.CharField(max_length=100)
    # 뮤비 업로드 날짜
    upload_date = models.DateTimeField(null = True)
    # 모델 생성 날짜
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Review(models.Model):
    # 작성자
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 내용
    text = models.TextField()
    # 뮤직비디오
    video = models.ForeignKey(
        MusicVideo, on_delete=models.CASCADE, related_name="reviews")
    # 평점
    score = models.FloatField()
    # 모델 생성 날짜
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
