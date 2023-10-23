from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_welcome(request):
    return HttpResponse('Welcome to eMobilis')

def about(request):
    return HttpResponse('About eMobilis')

def timetable(request):
    return HttpResponse('This is the time table')

def note(request):
    return HttpResponse('Hii code ilinisumbua')


