from django.shortcuts import render
from mv.models import MusicVideo
from director.models import Director

# Create your views here.
def home(request):
    mv1 = MusicVideo.objects.get(pk="100")
    mv2 = MusicVideo.objects.get(pk="200")
    return render(request, 'home.html', { 'mv1': mv1, 'mv2': mv2 })

def errorPage(request):
    return render(request, '404.html')