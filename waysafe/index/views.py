from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #always put in request
    template_name = 'index/index.html'
    return render(request,template_name)

def myOrders(request):
    return HttpResponse("<h1>This is my orders </h1>")

def myAccount(request):
    return HttpResponse("<h1>This is My Account </h1>")

def help(request):
    return HttpResponse("<h1>This is help </h1>")

def myCart(request):
    return HttpResponse("<h1>This is my cart</h1>")

def aisles(request):
    return HttpResponse("<h1>This is aisle</h1>")

