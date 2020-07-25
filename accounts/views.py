from django.shortcuts import render

# Create your views here.

def signIn(request):
    return render(request, 'signIn.html')

def signUp(request):
    return render(request, 'signUp.html')

def myPage(request):
    return render(request, 'myPage.html')