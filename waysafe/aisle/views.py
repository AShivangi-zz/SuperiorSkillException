from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
from cart.models import cart


# Create your views here.
# Create your views here.
def index(request): #always put in request
    template_name = 'aisle/index.html'
    return render(request,template_name)

def aisle(request):
    return HttpResponse("<h1>This is the categories</h1>")

@login_required
def add_to_cart(request,item_name):

    item = get_object_or_404(item, pk = item_name)
    cart, created = cart.objects.get_or_create(user=request.user,active = True)
    cart.save()
    message.success(request, "Added" + item_name + " to cart!")

def babycare_item(request):
    babycareitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Baby Care"')
    template_name = 'aisle/babycare.html'
    context = {"babycareitems": babycareitems}
    return render(request,template_name, context)

def beverage_item(request):
    beverageitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Beverages"')
    template_name = 'aisle/beverages.html'
    context = {"beverageitems": beverageitems}
    return render(request, template_name, context)

def meat_item(request):
    meatitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Meat"')
    template_name = 'aisle/meat.html'
    context = {"meatitems": meatitems}
    return render(request,template_name, context)

def frozen_item(request):
    frozenitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Frozen"')
    template_name = 'aisle/frozen.html'
    context = {"frozenitems": frozenitems}
    return render(request,template_name, context)

def pasta_item(request):
    pastaitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Pasta"')
    template_name = 'aisle/pasta.html'
    context = {"pastaitems": pastaitems}
    return render(request,template_name, context)

def dairy_item(request):
    dairyitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Dairy"')
    template_name = 'aisle/dairy.html'
    context = {"dairyitems": dairyitems}
    return render(request,template_name, context)

def snacks_item(request):
    snacksitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Snacks"')
    template_name = 'aisle/snacks.html'
    context = {"snacksitems": snacksitems}
    return render(request,template_name, context)

def alcohol_item(request):
    alcoholitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Alcohol"')
    template_name = 'aisle/alcohol.html'
    context = {"alcoholitems": alcoholitems}
    return render(request,template_name, context)