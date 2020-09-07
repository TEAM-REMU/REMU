from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
# Create your views here.

def login(request):
    
    if request.method == "POST":
       
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):

    if request.method == "POST":
        if request.POST["password"] == request.POST["re_password"]:
            user = User.objects.create_user(
                username = request.POST['username'], password = request.POST['password'], email = request.POST['email'])
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')

    return render(request, 'signup.html')

def my_page(request, id):
    return render(request, 'my_page.html')
