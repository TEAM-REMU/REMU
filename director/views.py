from django.shortcuts import render

# Create your views here.
def director_list(request):
    return render(request, 'director_list.html')

<<<<<<< HEAD
def directorProfile(request):
    return render(request, 'directorProfile.html')
=======
def director_profile(request, id):
    return render(request, 'director_profile.html')
>>>>>>> 5070472aade9d541d55f1a4f25bd1d1e9ccd619f
