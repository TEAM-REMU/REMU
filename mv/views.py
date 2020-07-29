from django.shortcuts import render
from .models import MusicVideo

# Create your views here.


def mvList(request):

    videos = MusicVideo.objects.all()

    return render(request, 'mvList.html', {'videos': videos})


def mvDetail(request, id):
    return render(request, 'mvDetail.html')
