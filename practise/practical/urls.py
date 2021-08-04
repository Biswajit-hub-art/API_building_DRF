from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path('articles/', article_list, name="articles"),
    path('article_detail/<int:id>', article_detail, name="detail"),
]