
from django.contrib import admin
from django.urls import path
import mv.views

urlpatterns = [
    path('', mv.views.mv_list, name="mv_list"),
    path('<int:id>', mv.views.mv_detail, name="mv_detail"),
    path('createReview/<int:mv_id>', mv.views.create_review, name="create_review"),
    path('review/<int:mv_id>', mv.views.get_review_for_mv,
         name="get_review_for_mv"),
]
