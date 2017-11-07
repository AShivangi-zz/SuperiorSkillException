from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #always put in request
    template_name = 'payment/index.html'
    return render(request,template_name)

def success(request):
    template_name= "payment/payment_successful.html"
    return render(request, template_name)
