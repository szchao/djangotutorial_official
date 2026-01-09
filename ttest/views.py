from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views import View

def index(request, x='world'):
    return HttpResponse('hello and ' + x )

def any_s(requt, any):
    return HttpResponse(any)

def main(rq):
    return HttpResponse("main page")

def danger(request):
    return HttpResponse(escape(request.GET['guess']))

def rest(request, guess):
    return HttpResponse(escape(guess))

class MainView(View):
    def get(self, request):
        return HttpResponse('from class based view')

class RestMainView(View):
    def get(self, request, guess):
        return HttpResponse(guess)
    
class GameView(View):
    def get(self, request, guess):
        x = {'guess': guess}
        return render(request, 'ttest/cond.html', x)

from django.views import generic
from .models import Cat

class CatListView(generic.ListView):
    model = Cat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(extra_info="Hello")
        context['crazy_thing'] = 'CRAZY THING'
        print("模板上下文内容：")
        for key, value in context.items():
            print(f"{key}: {value}")
        return context

class CatDetailView(generic.DetailView):
    model = Cat
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for key, value in context.items():
            print(f"{key}: {value}")
        return context