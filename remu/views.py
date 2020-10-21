from django.shortcuts import render
from mv.models import MusicVideo, Review
from director.models import Director
from django.shortcuts import get_object_or_404


# Create your views here.d（（（（
def home(request):
    director1 = Director.objects.get(name='이래경')
    director2 = Director.objects.get(name='황수아')
    music_video = MusicVideo.objects.get(title="좋아해(bye) (Love You (bye))")
    return render(request, 'home.html', {"director1" : director1, "director2" : director2, "music_video" : music_video})


def errorPage(request):
    return render(request, '404.html')