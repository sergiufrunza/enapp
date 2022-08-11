from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.views import generic
from django.views.generic.base import TemplateView, View
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.shortcuts import *
from django.http import JsonResponse
from django.template import RequestContext
from pyexpat.errors import messages

from .models import *
from .source import *
from .forms import *
from .utils import *
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


class LevelView(DataMixin, TemplateView):
    template_name = 'home/TemplateLevel.html'
    pk_url_kwarg = 'lvl'
    model = UserProfile
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if len(Buffer({}, 0)):
            Puser = UserProfile.objects.get(user=self.request.user)
            context = Buffer({}, 0)
            point = True
            for word in context['en']:
                if not word['correct']:
                    point = False
            if point:
                Puser.correct += 1
            else:
                Puser.incorrect += 1
            Puser.save()
            Buffer({}, 2)
        else:
            x = random.randint(0, len(dictionary) - 1)
            context['md'] = dictionary[x]['md']
        c_def = self.get_user_context(title="Level"+str(kwargs['lvl']))
        return dict(list(context.items()) + list(c_def.items()))


class MainView(DataMixin, ListView):
    template_name = 'home/homepage.html'
    model = Level
    context_object_name = "level"

    def get_queryset(self):
        return Level.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        c_def = self.get_user_context(title="EnApp")
        context = super().get_context_data(**kwargs)
        return dict(list(context.items())+list(c_def.items()))


def GetAnswer( request):
    en = request.GET.get("en")
    md = request.GET.get("md")
    return JsonResponse(Buffer(CheckWords(en, md),1))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'home/loginregistrate.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Log In")
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class LoginUserTemplate(DataMixin, LoginView):
    form_class = AuthenticationFormPers
    template_name = 'home/loginregistrate.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sing In")
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')



def Log_Out_User(request):
    logout(request)
    return redirect("home")




class ProfileUser(DataMixin, TemplateView):
    template_name = 'home/Profile.html'
    model = UserProfile
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['user'] = UserProfile.objects.get(user=self.request.user)
        c_def = self.get_user_context(title=user.user_name)
        answers = user.correct + user.incorrect
        if answers:
            context["correct"] = (user.correct/answers)*100
            context["incorrect"] = (user.incorrect/answers)*100
        else:
            context["correct"] = 0
            context["incorrect"] = 0
        context['user'] = user
        return dict(list(context.items())+list(c_def.items()))

class ProfileUsers(DataMixin, TemplateView):
    template_name = 'home/PreviewUser.html'
    model = UserProfile
    pk_url_kwarg = 'pk'
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['user'] = UserProfile.objects.get(pk=kwargs['pk'])
        c_def = self.get_user_context(title=user.user_name)
        answers = user.correct + user.incorrect
        if answers:
            context["correct"] = (user.correct/answers)*100
            context["incorrect"] = (user.incorrect/answers)*100
        else:
            context["correct"] = 0
            context["incorrect"] = 0
        context['user'] = user
        return dict(list(context.items())+list(c_def.items()))

@login_required
@transaction.atomic
def EditProfileUser(request):
    if request.method == 'POST':
        profile_form = ProfileDate(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = ProfileDate(instance=request.user.userprofile)
    if request.user.userprofile.user_name:

        data = {
        'profile_form': profile_form,
        'title': "Edit" + request.user.userprofile.user_name
    }
    else:
        data = {
            'profile_form': profile_form,
            'title': "Edit"
        }
    return render(request, 'home/ProfileEdit.html', data)





def CheckWords(en, md):
    getenarray = en.split()
    for a in dictionary:
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
