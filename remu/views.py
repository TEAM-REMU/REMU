from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def errorPage(request):
    return render(request, '404.html')