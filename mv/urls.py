
from django.contrib import admin
from django.urls import path
import mv.views

urlpatterns = [
    path('', mv.views.mv_list, name="mvList"),
    path('<int:id>', mv.views.mv_detail, name="mvDetail"),
    path('createReview/<int:mv_id>', mv.views.create_review, name="create_review"),
]
