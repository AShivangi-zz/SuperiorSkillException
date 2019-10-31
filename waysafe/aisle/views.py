from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from cart.models import cart

from django.template import loader

# Create your views here.
# Create your views here.
def index(request): #always put in request
    template_name = 'aisle/index.html'
    return render(request,template_name)

def aisle(request):
    return HttpResponse("<h1>This is the categories</h1>")

def babycare_item(request):

    c = cart()
    babycareitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Baby Care"')
    template_name = 'aisle/babycare.html'

    context = {"babycareitems": babycareitems}

    if request.is_ajax():
        requestajax = request.POST.get('key')
        requestajaxamount = request.POST.get('amount')
        c.item_list = requestajax
        c.quantity = requestajaxamount
        c.save()
        #return render(request, 'aisle/beverages.html')

    return render(request,template_name, context)

def beverage_item(request):
    beverageitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Beverages"')
    template_name = 'aisle/beverages.html'
    context = {"beverageitems": beverageitems}

    c = cart()
    if request.is_ajax():
        requestajax = request.POST.get('key')
        requestajaxamount = request.POST.get('amount')
        c.item_list = requestajax
        c.quantity = requestajaxamount
        c.save()
    return render(request, template_name, context)

def meat_item(request):
    meatitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Meat"')
    template_name = 'aisle/meat.html'
    context = {"meatitems": meatitems}

    c = cart()
    if request.is_ajax():
        requestajax = request.POST.get('key')
        requestajaxamount = request.POST.get('amount')
        c.item_list = requestajax
        c.quantity = requestajaxamount
        c.save()
    return render(request,template_name, context)

def frozen_item(request):
    frozenitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Frozen"')
    template_name = 'aisle/frozen.html'
    context = {"frozenitems": frozenitems}

    c = cart()
    if request.is_ajax():
        requestajax = request.POST.get('key')
        requestajaxamount = request.POST.get('amount')
        c.item_list = requestajax
        c.quantity = requestajaxamount
        c.save()
    return render(request,template_name, context)

def pasta_item(request):
    pastaitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Pasta"')
    template_name = 'aisle/pasta.html'
    context = {"pastaitems": pastaitems}

    c = cart()
    if request.is_ajax():
        requestajax = request.POST.get('key')
        requestajaxamount = request.POST.get('amount')
        c.item_list = requestajax
        c.quantity = requestajaxamount
        c.save()
    return render(request,template_name, context)

def dairy_item(request):
    dairyitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Dairy"')
    template_name = 'aisle/dairy.html'
    context = {"dairyitems": dairyitems}
    c = cart()
    if request.is_ajax():
        requestajax = request.POST.get('key')
        requestajaxamount = request.POST.get('amount')
        c.item_list = requestajax
        c.quantity = requestajaxamount
        c.save()
    return render(request,template_name, context)

def snacks_item(request):
    snacksitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Snacks"')
    template_name = 'aisle/snacks.html'
    context = {"snacksitems": snacksitems}

    c = cart()
    if request.is_ajax():
        requestajax = request.POST.get('key')
        requestajaxamount = request.POST.get('amount')
        c.item_list = requestajax
        c.quantity = requestajaxamount
        c.save()
    return render(request,template_name, context)

def alcohol_item(request):
    alcoholitems = Item.objects.raw('SELECT * FROM aisle_item WHERE category = "Alcohol"')
    template_name = 'aisle/alcohol.html'
    context = {"alcoholitems": alcoholitems}

    c = cart()
    if request.is_ajax():
        requestajax = request.POST.get('key')
        requestajaxamount = request.POST.get('amount')
        c.item_list = requestajax
        c.quantity = requestajaxamount
        c.save()
    return render(request,template_name, context)