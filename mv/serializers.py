from rest_framework import serializers
from .models import Review
from django.contrib.auth.models import User
from accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):

    # profile = ProfileSerializer(read_only=True)

    profile = serializers.CharField(
        source='profile.name', read_only=True)

    class Meta:
        model = User
        fields = ['profile']


class ReviewSerializer(serializers.ModelSerializer):
    # author_name = serializers.CharField(
    #     source='author.user.profile.name', read_only=True)

    author = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['text', 'video', 'score', 'register_date', 'author']
