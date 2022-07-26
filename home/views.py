
from django.shortcuts import *
from django.http import JsonResponse, HttpResponse
from django.template import RequestContext
from . import source
import random
import json
def index(request):
    x = random.randint(0, len(source.dictionary)-1)
    if request.GET.get("en"):
        geten = request.GET.get("en")
        getmd = request.GET.get("md")
        data = checkwords(geten, getmd)
        data['logged'] = True
        return render(request, 'home/homepage.html', context=data)

    elif request.GET.get('logged') and not request.GET.get("en"):
        data = {}
        data['logged'] = True
        data['md'] = source.dictionary[x]["md"]
        return render(request, 'home/homepage.html', context=data)
    else:
        data = {
            "md": source.dictionary[x]["md"]
        }
        return render(request, 'home/homepage.html')







def checkwords(en ,md):

    getenarray = en.split()
    for a in source.dictionary:
        if a['md'] == md:
            getenoriginarray = a['en'].split()
            if len(getenarray) > len(getenoriginarray) or len(getenarray) == len(getenoriginarray):
                arrayparent = getenoriginarray
            else:
                arrayparent = getenarray

            for b in range(len(arrayparent)):
                if getenarray[b] != getenoriginarray[b]:
                    getenarray[b] = {
                        "correct": False,
                        "word": getenarray[b]
                    }
                else:
                    getenarray[b] = {
                        "correct": True,
                        "word": getenarray[b]
                    }


    data = {
        "md": md,
        "en": getenarray
    }
    return data