from django.shortcuts import render
from django.http import HttpResponse
from cart.models import cart
from aisle.models import Item

# Create your views here.
def index(request): #always put in request
    template_name = 'payment/index.html'
    return render(request,template_name)

def success(request):
    template_name= "payment/payment_successful.html"
    total = 0.0
    cartitemsid = cart.objects.raw('SELECT * from cart_cart INNER JOIN aisle_item ON aisle_item.id = item_list')

    for i in cartitemsid:
        total = total + float(i.price)

    offer = total - (0.10*total)

    context = {"cartitemsid": cartitemsid, "total": offer}
    return render(request, template_name, context)
