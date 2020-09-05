import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "remu.settings")
import django
django.setup()
from director.models import *
from mv.models import *
import csv
import datetime

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
        # 프로덕션이 있는 경우 
        # 외래키 물려주기 위해서 데이터 조회해서 해당 프로덕션 가져오기
        if(len(data[i][3])):
            pre_production = Production.objects.get(name = data[i][3], image_url = data[i][4])
            
            director, created = Director.objects.get_or_create(
                name = data[i][0],
                production = pre_production,
                sns_link = data[i][2],
                image_url = data[i][1]
            )
        # 프로덕션이 없는 경우    
        elif(len(data[i][3]) == 0):
            director, created = Director.objects.get_or_create(
                name = data[i][0],
                sns_link = data[i][2],
                image_url = data[i][1]
            )
       


# DB에 뮤비 저장
for i in range(1, len(data)):
    # 뮤비 제목이 있는지 체크
    if(len(data[i][5])):
        # 해당 뮤비의 프로덕션이 있는 경우
        if(len(data[i][3])):
            pre_production = Production.objects.get(name = data[i][3], image_url = data[i][4])
        if(len(data[i][0])):
            pre_director = Director.objects.get(name = data[i][0], sns_link = data[i][2], image_url = data[i][1])
        
        #감독이 없는 경우 프로덕션만 있을 때
        if(len(data[i][0]) == 0):
            music_video, created = MusicVideo.objects.get_or_create(
                title = data[i][5],
                production = pre_production,
                video_link = data[i]6],
                artist = data[i][7],[
                upload_date = datetime.datetime.strptime(data[i][8], '%Y-%m-%d')
            )

        #감독이 있는 경우 프로덕션과 상관없이 감독만 외래키 물리면 돼
        elif(len(data[i][0])):
                music_video, created = MusicVideo.objects.get_or_create(
                title = data[i][5],
                director = pre_director,
                video_link = data[i][6],
                artist = data[i][7],
                upload_date = datetime.datetime.strptime(data[i][8], '%Y-%m-%d')
            )


