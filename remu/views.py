from django.shortcuts import render
from mv.models import MusicVideo, Review
from director.models import Director, Production
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    director1 = Director.objects.get(name='이래경')
    director2 = Director.objects.get(name='최용석(Yong Seok Choi)')
    production1 = Production.objects.get(name='리전드 필름(Rigend Film)')
    director3 = Director.objects.get(name='황수아')
    music_video = MusicVideo.objects.get(title="좋아해(bye) (Love You (bye))")
    return render(request, 'home.html', {"director1" : director1, "director2" : director2, "production1" : production1, "director3" : director3, "music_video" : music_video})


def errorPage(request):
    return render(request, '404.html')