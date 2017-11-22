from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from cart.models import cart
from aisle.models import Item

# Create your views here.
# Create your views here.
@login_required(login_url='/register/')
def index(request): #always put in request
    template_name = 'history/index.html'
    return render(request,template_name)

def completeList(request):
    cartitemsid = cart.objects.raw('SELECT * from cart_cart INNER JOIN aisle_item ON aisle_item.id = item_list')

    context = {"cartitemsid": cartitemsid}

    template_name = 'history/completeList.html'
    return render(request, template_name, context)


def editingList(request):
    template_name = 'history/editingList.html'
    return render(request, template_name)


def previousOrders(request):
    return HttpResponse("<h1>This is the previous order</h1>")

def savedItems(request):
    return HttpResponse("<h1>This is the saved items</h1>")

def lastOrder(request): #always put in request

    cartitemsid  = cart.objects.raw('SELECT * from cart_cart INNER JOIN aisle_item ON aisle_item.id = item_list')

    context = {"cartitemsid": cartitemsid}

    template_name = 'history/lastOrder.html'
    return render(request,template_name, context)
