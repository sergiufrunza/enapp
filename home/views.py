
from django.shortcuts import render


def index(request):
    return render(request, 'home/homepage.html')
# Create your views here.
