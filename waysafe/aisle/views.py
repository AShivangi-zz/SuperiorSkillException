from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def index(request): #always put in request
    template_name = 'aisle/index.html'
    return render(request,template_name)

def aisle(request):

    return HttpResponse("<h1>This is the categories</h1>")
