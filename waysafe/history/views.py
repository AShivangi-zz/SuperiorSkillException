from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# Create your views here.
@login_required(login_url='/register/')
def index(request): #always put in request
    template_name = 'history/index.html'
    return render(request,template_name)

def lastOrder(request):
    template_name = 'history/lastOrder.html'
    return render(request, template_name)

def completeList(request):
    template_name = 'history/completeList.html'
    return render(request, template_name)

def editingList(request):
    template_name = 'history/editingList.html'
    return render(request, template_name)


def previousOrders(request):
    return HttpResponse("<h1>This is the previous order</h1>")

def savedItems(request):
    return HttpResponse("<h1>This is the saved items</h1>")
