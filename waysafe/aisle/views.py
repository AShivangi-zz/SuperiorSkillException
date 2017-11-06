from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
# Create your views here.
def index(request): #always put in request
    template_name = 'aisle/index.html'
    return render(request,template_name)

def aisle(request):
    return HttpResponse("<h1>This is the categories</h1>")


def baby_care_subcategory(request):
    template_name = 'aisle/babycare.html'
    return render(request, template_name)

def beverages_subcategory(request):
    template_name = 'aisle/beverages.html'
    return render(request, template_name)

def dairy_subcategory(request):
    template_name = 'aisle/dairy.html'
    return render(request, template_name)

def frozen_subcategory(request):
    template_name = 'aisle/frozen_subcategory.html'
    return render(request, template_name)

def meat_subcategory(request):
    template_name = 'aisle/meat_subcategory.html'
    return render(request, template_name)

def pasta_and_grains_subcategory(request):
    template_name = 'aisle/pasta_and_grains_subcategory.html'
    return render(request, template_name)

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