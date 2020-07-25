from django.shortcuts import render

# Create your views here.
def directorList(request):
    return render(request, 'directorList.html')

def directorProfile(request, id):
    return render(request, 'directorProfile.html')