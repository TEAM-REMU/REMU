from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Review, MusicVideo

from django.core.paginator import Paginator, PageNotAnInteger

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
    auth.logout(request)
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

        # 비밀번호 재입력 일치 여부 확인
        if request.POST['password'] != request.POST['re_password']:
            return render(request, 'signup.html', {'error_2': '비밀번호와 비밀번호 재입력이 일치하지 않습니다'})

        # 닉네임 글자수 제한(2-10자)
        nickname_len = len(request.POST['nickname'])
        if nickname_len > 10 or nickname_len < 2:
            return render(request, 'signup.html', {'error_0': '글자수가 2이상 10이하여야 합니다.'})

        # 닉네임 중복 검사
        signuped_user_profile = Profile.objects.filter(nickname=request.POST["nickname"])
        if len(signuped_user_profile) >= 1:
            return render(request, 'signup.html', {'error_3': '존재하는 닉네임입니다'})

        # 유저 프로필 생성
        profile = Profile()
        user = User.objects.create_user(
            username = request.POST['username'], password = request.POST['password'], email = request.POST['email']
        )
        profile.user = user
        profile.nickname = request.POST["nickname"]
        
        # 프로필 사진 확인
        if 'image' in request.FILES:
            profile.image = request.FILES['image']

        profile.save()
        auth.login(request, user)
        return redirect('home')
    else:
        return render(request, 'signup.html')

def my_page(request, id):
    profile = Profile.objects.get(pk=id)
    
    review_list = Review.objects.filter(author=profile.user)
    print(review_list)

    review_cnt = Review.objects.filter(author=profile.user).count()
    print(review_cnt)

    
    page = request.GET.get('page', 1)
    paginator = Paginator(review_list, 25)
    reviews = paginator.get_page(page)

    return render(request, 'my_page.html', {'profile':profile, 'reviews':reviews, 'review_list':review_list, 'review_cnt':review_cnt})


def update(request, id):
    profile = get_object_or_404(Profile, pk = id)
   
    if request.method == 'POST':
        # 프로필 사진 변경
        if 'image' in request.FILES:
            profile.image = request.FILES['image']

        # 닉네임 글자수 제한
        nickname_len = len(request.POST['nickname'])
        if nickname_len > 10 or nickname_len < 2:
            return render(request, 'profile_update.html', {'error_0': '글자수가 2이상 10이하여야 합니다.'})

        # 닉네임 중복 검사
        profile.newnickname = request.POST['nickname']
        signuped_user_profile = Profile.objects.filter(nickname=request.POST["nickname"])

        if len(signuped_user_profile) >= 1:
            if profile.nickname != profile.newnickname:
                return render(request, 'profile_update.html', {'profile':profile, 'error_3': '존재하는 닉네임입니다'})
            profile.nickname = profile.newnickname

        # 비밀번호 중복 검사
        profile.password = request.POST['password']
        profile.re_password = request.POST['re_password']
        
        if profile.password != profile.re_password:
            return render(request, 'profile_update.html', {'profile':profile, 'error_2': '비밀번호와 비밀번호 확인이 일치하지 않습니다'})
        
        profile.save()
        return redirect('my_page', profile.id)
    
    else:
        return render(request, 'profile_update.html',{'profile':profile})