from django.views.generic.base import TemplateView
from django.shortcuts import *
from django.http import JsonResponse
from django.template import RequestContext
from home.models import *
from . import source
import random

Date = {}


def Buffer(answer, n):
    global Date
    if n == 1:
        Date = answer
        return Date
    elif n == 2:
        Date = {}
    if n == 0:
        return Date


class MainView(TemplateView):
    template_name = 'home/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if len(Buffer({}, 0)):
            context = Buffer({}, 0)
            Buffer({}, 2)
        else:
            x = random.randint(0, len(source.dictionary) - 1)
            context['md'] = source.dictionary[x]['md']
        return context


def GetAnswer(request):
    en = request.GET.get("en")
    md = request.GET.get("md")
    return JsonResponse(Buffer(CheckWords(en, md),1))


def CheckWords(en, md):
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
