from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World. You are at the polls index')

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def result(request, question_id):
    response = f"you're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"you're voting on the question {question_id}")