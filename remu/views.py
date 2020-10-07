from django.shortcuts import render
from mv.models import MusicVideo
from director.models import Director
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    #mv1 = MusicVideo.objects.get(pk="100")
    #MusicVideo.objects.get_object_or_404(pk="100")
    return render(request, 'home.html')
    #, { 'mv1': mv1 })


def errorPage(request):
    return render(request, '404.html')