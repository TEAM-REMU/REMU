import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "remu.settings")
import django
django.setup()
from director.models import *
from mv.models import *
import csv
import datetime
import re

file_name = 'data'
# wr.writerow(['감독 이름', '감독 이미지 주소', '감독 SNS 링크', '프로덕션 이름', '프로덕션 이미지 주소', '뮤비 제목', '뮤비 주소', 
    # '아티스트', '뮤비 업로드 날짜'])

#데이터 파일 열기
with open(f'{file_name}.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    data=list(csv.reader(csvDataFile))



# DB에 프로덕션 저장
for i in range(1, len(data)):
    # 프로덕션이 있는지 체크
    if(len(data[i][3])):
        production, created = Production.objects.get_or_create(
            name = data[i][3],
            image_url = data[i][4]
        )


# DB에 감독 저장
for i in range(1, len(data)):
    # 감독이 있는지 체크
    if(len(data[i][0])):
        # 일단 프로덕션을 제외하고 감독 저장
        director, created = Director.objects.get_or_create(
            name = data[i][0],
            sns_link = data[i][2],
            image_url = data[i][1]
        )
        
        # 프로덕션이 있고 감독 객체에 프로덕션이 비어있는 경우
        if(len(data[i][3]) and director.production is None):
            # 외래키 물려주기 위해서 데이터 조회해서 해당 프로덕션 가져오기
            pre_production = Production.objects.get(name = data[i][3], image_url = data[i][4])
            director.production = pre_production
            director.save()


#으으으으으으 csv파일 너무 지저분해역!!!
upload_date_pattern = re.compile('\d{4,}-\d{1,2}-\d{1,2}') 

# DB에 뮤비 저장
for i in range(1, len(data)):
    # 뮤비 제목이 있는지 체크
    if(len(data[i][5])):
        # 일단 감독, 프로덕션 생각하지 않고 뮤비 저장하기
        music_video, created = MusicVideo.objects.get_or_create(
            title = data[i][5],
            video_link = data[i][6],
            artist = data[i][7]
        )
        # upload_date가 말썽입니다 여러분~ 더 얘기해봐요! 호호!
        if(upload_date_pattern.match(data[i][8]) is not None):
            music_video.upload_date = datetime.datetime.strptime(data[i][8], '%Y-%m-%d')
            music_video.save()

        #감독이 없고 프로덕션만 있는데 프로덕션이 아직 저장 안됐을때 
        if(len(data[i][0]) == 0 and music_video.production is None):
            pre_production = Production.objects.get(name = data[i][3], image_url = data[i][4])
            music_video.production = pre_production
            music_video.save()

        #감독이 있는데 아직 저장 안됐을때
        elif(len(data[i][0]) and music_video.director is None):
            pre_director = Director.objects.get(name = data[i][0], sns_link = data[i][2], image_url = data[i][1])
            music_video.director = pre_director
            music_video.save()