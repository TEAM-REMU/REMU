from django.shortcuts import render

# Create your views here.
def director_list(request):
    return render(request, 'director_list.html')

def director_profile(request, id):
    return render(request, 'director_profile.html')