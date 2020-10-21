from django.shortcuts import render
from mv.models import MusicVideo, Review
from director.models import Director, Production
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    director1 = Director.objects.get(name='이래경')
    production1 = Production.objects.get(name='룸펜스(Lumpens)')
    production2 = Production.objects.get(name='리전드 필름(Rigend Film)')
    director2 = Director.objects.get(name='황수아')
    music_video = MusicVideo.objects.get(title="좋아해(bye) (Love You (bye))")
    return render(request, 'home.html', {"director1" : director1, "production1" : production1, "production2" : production2, "director2" : director2, "music_video" : music_video})


def errorPage(request):
    return render(request, '404.html')