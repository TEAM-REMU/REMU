from django.shortcuts import render, redirect
from director.models import Director, Production
from mv.models import MusicVideo
from django.db.models import Count
# Create your views here.


def count_reviews(directors):
    musicvideos = MusicVideo.objects.filter(director=d)
    for mv in musicvideos:
        print(mv.reviews.count())
    directors['a'] = 'asdfdsf'
    return directors


def result(request):
    search = request.GET.get("search", "")
    # 제목 일치 뮤비
    mv_from_title = MusicVideo.objects.filter(title__contains=search)
    # 가수 일치 뮤비
    mv_from_artist = MusicVideo.objects.filter(artist__contains=search)
    # 두개 합침
    mv = mv_from_artist.union(mv_from_title)

    # 감독 이름 일치
    director_from_director_name = Director.objects.filter(
        name__contains=search)

    # 프로덕션 이름 일치
    production_from_production_name = Production.objects.filter(
        name__contains=search)
    # 속한 감독 있는 프로덕션에 속한 감독들의 id
    director_id_from_production = production_from_production_name.filter(
        director__isnull=False).values_list('director')
    # 위에서 구한 id와 일치하는 감독들
    director_from_production = Director.objects.filter(
        id__in=director_id_from_production)
    # 속한 감독이 없는 프로덕션들
    production_from_production_name = production_from_production_name.filter(
        director__isnull=True)

    director = director_from_director_name.union(director_from_production)

    director_list = []

    for d in director:
        musicvideos = MusicVideo.objects.filter(director=d)
        count = 0
        my_director = d.__dict__
        for mv in musicvideos:
            count += mv.reviews.count()
        my_director['count'] = count
        director_list.append(my_director)

    production = production_from_production_name

    production_list = []

    for p in production:
        musicvideos = MusicVideo.objects.filter(production=p)
        count = 0
        my_director = p.__dict__
        for mv in musicvideos:
            count += mv.reviews.count()
        my_director['count'] = count
        director_list.append(my_director)

    print('속한 감독 없는 프로덕션', production_from_production_name)
    print('프로덕션에 속한 감독', director_from_production)

    print('뮤비', mv)
    print('감독', director_list)
    print('프로덕션', production_list)

    return render(request, 'result.html')
