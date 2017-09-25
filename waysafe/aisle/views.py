from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def index(request): #always put in request
    return HttpResponse("<h1>This is the WaySafe app aisle</h1>")

def aisle(request):

    return HttpResponse("<h1>This is the categories</h1>")
