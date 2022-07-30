from django.contrib import admin
from django.urls import path, include, re_path
from home.views import *

urlpatterns = [
    path('', MainView.as_view(), name="home"),
    re_path(r'answer/', GetAnswer),

]