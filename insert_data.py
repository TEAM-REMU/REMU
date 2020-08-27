import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "remu.settings")
import django
django.setup()
from director.models import *
from mv.models import *
import csv
from datetime import datetime

file_name = 'data'

with open(f'{file_name}.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    data=list(csv.reader(csvDataFile))

    for i in range(1, len(data)):
        # DB에 프로덕션 저장
        production = Production()
        production.name = data[i][1]
        production.save()

        # DB에 감독 저장
        director = Director()
        director.name = data[i][0]
        director.production = production
        director.imageURL = data[i][2]
        director.save()

        # DB에 뮤비 저장
        music_video = MusicVideo()
        music_video.title = data[i][3]
        music_video.director = director
        music_video.production = production
        music_video.artist = data[i][4]
        music_video.upload_date = datetime.strptime(data[i][5], '%Y-%m-%d')
        music_video.save()