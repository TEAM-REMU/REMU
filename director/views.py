from django.shortcuts import render
from director.models import *
from mv.models import *
from django.db.models import Count
from django.http import HttpRequest
from django.core.paginator import Paginator

# Create your views here.
def director_list(request):
    return render(request, 'director_list.html')

def director_profile(request, id):
    director = Director.objects.get(pk=id)      
    mv_list = MusicVideo.objects.filter(director = director)
    if(request.path.split('/')[-1] == 'popular_ordered_mv'):
        popular_ordered_mv_list = mv_list.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')
        paginator = Paginator(popular_ordered_mv_list, 9)
        page = request.GET.get('page')
        mv_page = paginator.get_page(page)
        num_reviews = 0
        for mv in mv_list:
            num_reviews += mv.reviews.count()
        sns_links = director.sns_link.split(',')
        if(director.production is not None):
            production_name = director.production.name
            return render(request, 'director_profile.html', {'director':director, 'mv_list':popular_ordered_mv_list, 'mv_page':mv_page, 
            'num_reviews':num_reviews, 'production_name':production_name, 'sns_links':sns_links})
        return render(request, 'director_profile.html', {'director':director, 'mv_list':popular_ordered_mv_list, 'mv_page':mv_page, 
        'num_reviews':num_reviews, 'sns_links':sns_links})
       
    elif(request.path.split('/')[-1] == 'latest_ordered_mv'):
        latest_ordered_mv_list = mv_list.order_by('-upload_date')
        paginator = Paginator(latest_ordered_mv_list, 9)
        page = request.GET.get('page')
        mv_page = paginator.get_page(page)
        num_reviews = 0
        for mv in mv_list:
            num_reviews += mv.reviews.count()
        sns_links = director.sns_link.split(',')
        if(director.production is not None):
            production_name = director.production.name
            return render(request, 'director_profile.html', {'director':director, 'mv_list':latest_ordered_mv_list, 'mv_page':mv_page, 
            'num_reviews':num_reviews, 'production_name':production_name, 'sns_links':sns_links})
        return render(request, 'director_profile.html', {'director':director, 'mv_list':latest_ordered_mv_list, 'mv_page':mv_page, 
        'num_reviews':num_reviews, 'sns_links':sns_links})        
       
    
    
      

def production_profile(request, id):
    production = Production.objects.get(pk=id)
    mv_list = MusicVideo.objects.filter(production = production)
    if(request.path.split('/')[-1] == 'popular_ordered_mv'):
        popular_ordered_mv_list = mv_list.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')
        paginator = Paginator(popular_ordered_mv_list, 9)
        page = request.GET.get('page')
        mv_page = paginator.get_page(page)
        num_reviews = 0
        for mv in mv_list:
            num_reviews += mv.reviews.count()
        sns_links = production.sns_link.split(',')
        return render(request, 'production_profile.html', {'production':production, 'mv_list':popular_ordered_mv_list, 'mv_page':mv_page, 
        'num_reviews':num_reviews, 'sns_links':sns_links})

    elif(request.path.split('/')[-1] == 'latest_ordered_mv'):
        latest_ordered_mv_list = mv_list.order_by('-upload_date')
        paginator = Paginator(latest_ordered_mv_list, 9)
        page = request.GET.get('page')
        mv_page = paginator.get_page(page)
        num_reviews = 0
        for mv in mv_list:
            num_reviews += mv.reviews.count()
        sns_links = production.sns_link.split(',')
        return render(request, 'production_profile.html', {'production':production, 'mv_list':latest_ordered_mv_list, 'mv_page':mv_page, 
        'num_reviews':num_reviews, 'sns_links':sns_links})



# def popular_ordered_mv_of_director(request,id):
#     director = Director.objects.get(pk = id)
#     mv_list = MusicVideo.objects.filter(director = director)
#     popular_ordered_mv_list = mv_list.annotate(num_reviews=Count('review')).order_by('-num_reviews')
#     return render(request, 'director_profile.html', {'popular_ordered_mv_list':popular_ordered_mv_list})

# def latest_ordered_mv_of_director(request, id):
#     mv_list = MusicVideo.objects.order_by('-upload_date')
#     return render(request, 'director_profile.html', {'latest_order_mv':mv_list})

# def popular_ordered_mv_of_production(request,id):
#     pro = Director.objects.get(pk = id)
#     mv_list = MusicVideo.objects.filter(director = director)
#     popular_ordered_mv_list = mv_list.annotate(num_reviews=Count('review')).order_by('-num_reviews')
#     return render(request, 'director_profile.html', {'popular_ordered_mv_list':popular_ordered_mv_list})

# def latest_ordered_mv_of_production(request, id):
#     mv_list = MusicVideo.objects.order_by('-upload_date')
#     return render(request, 'director_profile.html', {'latest_order_mv':mv_list})


# def filter_order_mv_of_director(request, id):
#     director = Director.objects.get(pk = id)
#     mv_list = MusicVideo.objects.filter(director = director)
#     if(request.path.split('/')[-1] == 'popular_ordered_mv'):
#         popular_ordered_mv_list = mv_list.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')
#         return render(request, 'director_profile.html', {'popular_ordered_mv_list':popular_ordered_mv_list})
#     elif(request.path.split('/')[-1] == 'latest_ordered_mv'):
#         latest_ordered_mv_list = mv_list.order_by('-upload_date')
#         return render(request, 'director_profile.html', {'latest_ordered_mv':latest_ordered_mv_list})
