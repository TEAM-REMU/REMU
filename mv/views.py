from django.shortcuts import render, redirect
from .models import MusicVideo, Review
from .serializers import ReviewSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

# Create your views here.


def mv_list(request):

    videos = MusicVideo.objects.all()
<<<<<<< HEAD
    return render(request, 'mvList.html', {'videos': videos})
=======

    return render(request, 'mv_list.html', {'videos': videos})
>>>>>>> d4d16c5cb78c5af8ee440b2499b449ac94455174


def mv_detail(request, id):
    try:
        video = MusicVideo.objects.get(pk=id)

        score = Review.objects.filter(
            video=id).aggregate(Avg('score'))['score__avg']
        if score is None:
            score = 0

        reviews = video.reviews.all()[:3]
        if request.user is None:
            return render(request, 'mv_detail.html', {'video': video, 'reviews': reviews, 'score': score})
        else:
            try:
                review = Review.objects.get(author=request.user.id)
                return render(request, 'mv_detail.html', {'video': video, 'reviews': reviews, 'score': score, 'review': review})
            except Review.DoesNotExist:
                return render(request, 'mv_detail.html', {'video': video, 'reviews': reviews, 'score': score})
    except MusicVideo.DoesNotExist:
        return redirect('/404')


@login_required(login_url='/accounts/login')
def create_review(request, mv_id):
    try:
        reviewCount = Review.objects.filter(author=request.user.id).count()
        if reviewCount > 0:
            print("이미 리뷰 작성한 유저")
            return redirect('mv_detail', mv_id)

        video = MusicVideo.objects.get(pk=mv_id)

        review = Review()
        # 로그인 과정 없으니 아무 유저나 가져와서 입력
        review.author = request.user
        review.video = video
        review.text = request.POST["text"]
        review.score = request.POST["score"]

        review.save()
        return redirect('mv_detail', mv_id)
    except MusicVideo.DoesNotExist:
        print("해당 뮤직비디오가 존재하지 않음")
        return redirect('mv_detail', mv_id)


@api_view(['GET'])
def get_review_for_mv(request, mv_id):
    if request.method == 'GET':
        chunk = int(request.GET.get('count', 0))
        reviews = Review.objects.filter(video=mv_id)[chunk:chunk+3]
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@login_required(login_url='/accounts/login')
def delete_review(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)
        mvId = review.video.id
        if review.author.id == request.user.id:
            review.delete()
        return redirect('mv_detail', mvId)
    except Review.DoesNotExist:
        return redirect('mv_detail', mvId)

@login_required(login_url='/accounts/login')
def edit_review(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)
        mvId = review.video.id
        if review.author.id == request.user.id:
            review.text = request.POST["text"]
            review.score = request.POST["score"]
            review.save()
        return redirect('mv_detail', mvId)
    except Review.DoesNotExist:
        return redirect('mv_detail', mvId)
