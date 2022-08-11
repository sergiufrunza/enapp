from django.contrib import admin
from django.urls import path, include, re_path
from home.views import *

urlpatterns = [

    path('', MainView.as_view(), name='home'),
    path('SingIn/', LoginUserTemplate.as_view(), name='SingIn'),
    path('LogIn/', RegisterUser.as_view(), name='LogIn'),
    path('LogOut/', Log_Out_User, name='LogOut'),
    re_path(r'answer-mgFWETBrxIzdJwwA/', GetAnswer),
    path('Profile/', ProfileUser.as_view(), name='Profile'),
    path('EditProfile/', EditProfileUser, name='EditProfile'),
    path('Level/<int:lvl>/', LevelView.as_view(), name="Level"),
    path('User/<int:pk>/', ProfileUsers.as_view(), name="User")
]