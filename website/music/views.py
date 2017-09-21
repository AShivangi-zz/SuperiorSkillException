from django.shortcuts import render
from django.http import HttpResponse

def index(request): #always put in request
    return HttpResponse("<h1>This is the music app homepage</h1>")

