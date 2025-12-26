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