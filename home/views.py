
from django.shortcuts import render
from django.http import JsonResponse
from . import source
import random

def index(request):
    x = random.randint(0, len(source.dictionary)-1)
    if "en" in request.GET:
        geten = request.GET.get("en")
        getmd = request.GET.get("md")
        getenarray =  geten.split()
        for a in source.dictionary:
            if a['md'] == getmd:
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

                print(getenarray)

        data = {
                "md": getmd,
                "en": getenarray
            }
        print(data)
        return render(request, 'home/homepage.html', context=data)

    else:
        data = {
            "md": source.dictionary[x]['md']
        }
    print(data)
    return render(request, 'home/homepage.html', context=data)



