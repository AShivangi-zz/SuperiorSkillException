from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #always put in request
    template_name = 'savings/index.html'
    return render(request,template_name)

def coupons(request):
    return HttpResponse("<h1>This is the coupons</h1>")

def offers(request):
    return HttpResponse("<h1>This is the Offers</h1>")

