from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def index(request): #always put in request
    return HttpResponse("<h1>This is the WaySafe app history</h1>")

def lastOrder(request):
    return HttpResponse("<h1>This is the last order</h1>")


def previousOrders(request):
    return HttpResponse("<h1>This is the previous order</h1>")

def savedItems(request):
    return HttpResponse("<h1>This is the saved items</h1>")
