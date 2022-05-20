from django.urls import path
from . import views

urlpatterns =[
    path("index/",views.index,name='index'),
    path("signup/",views.register,name="signup"),
    path('room/<str:room_name>/',views.room,name="room"),
     path('room/kr/',views.room,name="room1"),
    path("login/",views.loginus,name="login"),
    path("newsfeed/",views.newsfeed,name="newsfeed"),
    path("like/<int:pk>",views.LikeView,name="like_post")
]