from django.shortcuts import render
from director.models import *
from mv.models import *

# Create your views here.
def director_list(request):
    return render(request, 'director_list.html')

def director_profile(request, id):
<<<<<<< Updated upstream
    return render(request, 'director_profile.html')
=======
    director = Director.objects.get(pk=id)      
    mv_list = MusicVideo.objects.filter(director = director)
    mv_count = mv.count()
    sns_links = director.sns_link.split(',')
    if(director.production is not None):
        production_name = director.production.name
        return render(request, 'director_profile.html', {'data':director, 'mv_list':mv_list, 'mv_count':mv_count, 'production_name':production_name, 'sns_links':sns_links})
    return render(request, 'director_profile.html', {'data':director, 'mv_list':mv_list, 'mv_count':mv_count, 'production_name':None, 'sns_links':sns_links})
      

def production_profile(request, id):
    production = Production.objects.get(pk=id)
    mv_list = MusicVideo.objects.filter(production = production)
    mv_count = mv.count()
    sns_links = production.sns_link.split(',')
    return render(request, 'director_profile.html', {'data':production, 'mv_list':mv_list, 'mv_count':mv_count, 'production_name':None, 'sns_links':sns_links})
>>>>>>> Stashed changes
