from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Review

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
            return render(request, 'login.html', {'error': '아이디나 비밀번호가 틀립니다.'})
    else:
        return render(request, 'login.html')  

def logout(request):
    django_logout(request)
    return redirect('home')

def signup(request):

    if request.method == "POST":
        # 아이디 글자수 제한(2-10자)
        username_len = len(request.POST['username'])
        if username_len > 10 or username_len < 2:
            return render(request, 'signup.html', {'error_0': '글자수가 2이상 10이하여야 합니다.'})
        
        # 아이디 중복 검사
        signuped_username = User.objects.filter(username=request.POST["username"])
        if len(signuped_username) >= 1:
            return render(request, 'signup.html', {'error_1': '존재하는 아이디입니다'})

        # 닉네임 글자수 제한(2-10자)
        nickname_len = len(request.POST['nickname'])
        if nickname_len > 10 or nickname_len < 2:
            return render(request, 'signup.html', {'error_0': '글자수가 2이상 10이하여야 합니다.'})

        # 닉네임 중복 검사
        signuped_user_profile = Profile.objects.filter(nickname=request.POST["nickname"])
        if len(signuped_user_profile) >= 1:
            return render(request, 'signup.html', {'error_2': '존재하는 닉네임입니다'})

        # 비밀번호 재입력 일치 여부 확인 & 유저 profile 생성
        if request.POST["password"] == request.POST["re_password"]:
            user = User.objects.create_user(
                username = request.POST['username'], password = request.POST['password'], email = request.POST['email'])
            profile = Profile()
            profile.user = user
            profile.nickname = request.POST["nickname"]
            profile.image = request.FILES['image']
            profile.save()
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')

    return render(request, 'signup.html')

def my_page(request, id):
    user = Profile.objects.get(pk=id)

    review = Review.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(review, 25)
    review_list = paginator.page_range

    return render(request, 'my_page.html', {'user':user, 'review':review, 'review_list':review_list})


def update(request, id):
    profile = get_object_or_404(Profile, pk = id)

    if request.method == 'POST':
        # 프로필 사진 변경
        if 'image' in request.FILES:
            profile.image = request.FILES['image']

        # 닉네임 글자수 제한
        nickname_len = len(request.POST['nickname'])
        if nickname_len > 10 or nickname_len < 2:
            return render(request, 'signup.html', {'error_0': '글자수가 2이상 10이하여야 합니다.'})

        # 닉네임 중복 검사
        profile.newnickname = request.POST['nickname']
        signuped_user_profile = Profile.objects.filter(nickname=request.POST["nickname"])

        if len(signuped_user_profile) >= 1:
            if profile.nickname != profile.newnickname:
                return render(request, 'profile_update.html', {'profile':profile, 'error_2': '존재하는 닉네임입니다'})
            profile.nickname = profile.newnickname
            profile.save()
            return redirect('my_page', profile.id)

        profile.nickname = profile.newnickname
        profile.save()
        return redirect('my_page', profile.id)

    else:
        return render(request, 'profile_update.html', {'profile' : profile})