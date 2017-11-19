from django.shortcuts import render
from django.http import HttpResponse
from .models import cart
from aisle.models import Item

# Create your views here.
# Create your views here.

def index(request): #always put in request


    total = 0.0

    #cartitemsid = cart.objects.raw('SELECT item_list from cart_cart')
    #cartitemsid  = cart.objects.raw('SELECT item_list, item_name, price from cart_cart INNER JOIN aisle_item '
      #                             'ON aisle_item.id = item_list')
    cartitemsid  = cart.objects.raw('SELECT * from cart_cart INNER JOIN aisle_item ON aisle_item.id = item_list')

   # for i in cartitemsid:
    #    test = Item.objects.raw('SELECT item_name, price from aisle_item WHERE id = i')
    #return HttpResponse(test)
    #
    for i in cartitemsid:
        total = total + float(i.price)

    context = {"cartitemsid": cartitemsid, "total": total}

    template_name = 'cart/index.html'
    return render(request,template_name, context)


