from django.shortcuts import render,HttpResponse
from datetime import datetime


def about_view(request):
    if request.method == 'GET':
        return HttpResponse('My name is Abibillaev Kanbolot, and Im 20')

def hobbies_view(request):
    if request.method == 'GET':
        return HttpResponse('I have several hobbies such as football playinng, language learning and reading')

def time_view(request):
    if request.method == 'GET':
        time_views = datetime.now()
        return HttpResponse(f"{time_views}")


