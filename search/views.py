from django.shortcuts import render, redirect
from director.models import Director, Production
from mv.models import MusicVideo
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.


def result(request):
    search = request.GET.get("search", "")
    order = request.GET.get("order", "popular")

    mv_count = 0
    # 제목 일치 뮤비
    mv_from_title = MusicVideo.objects.filter(
        title__contains=search).annotate(num_reviews=Count('reviews'))
    mv_count += MusicVideo.objects.filter(
        title__contains=search).count()
    # 가수 일치 뮤비
    mv_from_artist = MusicVideo.objects.filter(
        artist__contains=search).annotate(num_reviews=Count('reviews'))
    mv_count += MusicVideo.objects.filter(
        artist__contains=search).count()
    # 두개 합침
    mv = mv_from_artist.union(mv_from_title)

    if order is 'new':
        mv = mv.order_by('-register_date')
        paginator = Paginator(mv, 9)
        page = request.GET.get('page')
        mv_page = paginator.get_page(page)
    else:
        mv = mv.order_by('-num_reviews')
        paginator = Paginator(mv, 9)
        page = request.GET.get('page')
        mv_page = paginator.get_page(page)

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

    if order is 'new':
        director_list.sort(key=(lambda x: x['register_date']), reverse=True)

    else:
        director_list.sort(key=(lambda x: x['count']), reverse=True)

    production = production_from_production_name

    production_list = []

    for p in production:
        musicvideos = MusicVideo.objects.filter(production=p)
        count = 0
        mv_production = p.__dict__
        for mv in musicvideos:
            count += mv.reviews.count()
        mv_production['count'] = count
        production_list.append(mv_production)

    if order is 'new':
        production_list.sort(key=(lambda x: x['register_date']), reverse=True)
    else:
        production_list.sort(key=(lambda x: x['count']), reverse=True)


    director_production_together = director_list + production_list
    paginator = Paginator(director_production_together, 9)
    page = request.GET.get('page')
    director_page = paginator.get_page(page)

    print('속한 감독 없는 프로덕션', production_from_production_name)
    print('프로덕션에 속한 감독', director_from_production)

    print('뮤비', mv)
    print('감독', director_list)
    print('프로덕션', production_list)
    print(mv_count, len(director_list), len(production_list))


    return render(request, 'mv_result.html', {'mv' : mv,'mv_count' : mv_count, 'director' : director_list, 'director_count' : len(director_list),
    'production' : production_list, 'production_count' : len(production_list),'search' : search, 'order':order,  'mv_page':mv_page, 'director_page':director_page})