from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('surveys/', views.surveys),
    path('users/', views.users),
]