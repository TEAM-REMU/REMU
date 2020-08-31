from django.shortcuts import render, redirect
from .models import MusicVideo

# Create your views here.


def mv_list(request):

    videos = MusicVideo.objects.all()

    return render(request, 'mvList.html', {'videos': videos})


def mv_detail(request, id):

    try:
        video = MusicVideo.objects.get(pk=id)
        return render(request, 'mvDetail.html', {'video': video})
    except MusicVideo.DoesNotExist:
        return redirect('/404')
