from django.shortcuts import render
from django.http import HttpResponse
from .models import cart
from aisle.models import Item
from django.http import HttpResponseRedirect

# Create your views here.
# Create your views here.

def index(request): #always put in request


    total = 0.0
    itemtotal =0.0

    #cartitemsid = cart.objects.raw('SELECT item_list from cart_cart')
    #cartitemsid  = cart.objects.raw('SELECT item_list, item_name, price from cart_cart INNER JOIN aisle_item '
      #                             'ON aisle_item.id = item_list')
    cartitemsid  = cart.objects.raw('SELECT * from cart_cart INNER JOIN aisle_item ON aisle_item.id = item_list')

   # for i in cartitemsid:
    #    test = Item.objects.raw('SELECT item_name, price from aisle_item WHERE id = i')
    #return HttpResponse(test)
    #
    for i in cartitemsid:
        itemtotal=float(i.price) * float(i.quantity)
        total = total + itemtotal

    context = {"cartitemsid": cartitemsid, "total": total}

    template_name = 'cart/index.html'
    print("This view was loaded")
    return render(request,template_name, context)


def delete_item(request, item_id):
    print("Item loaded")
    print(item_id)
    item = cart.objects.get(id=item_id)
    item.delete()

    return HttpResponseRedirect("/cart")




