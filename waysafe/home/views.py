from django.shortcuts import render
from django.http import HttpResponse

"""
views are just python functions.

what they do is take user requests and gives them back something.

for the most part, user's will request the webpage so you will just give them the webpage using the function.

"""


# Create your views here.
def index(request): #always put in request
    return HttpResponse("<h1>This is the WaySafe app homepage</h1>")
