from django.shortcuts import render

# Create your views here.
def mvList(request):
    return render(request, 'mvList.html')

def mvDetail(request, id):
    return render(request, 'mvDetail.html')