from django.shortcuts import render
from django.http import HttpResponse
from aisle.models import Item

# Create your views here.
def index(request): #always put in request
    template_name = 'index/index.html'
    return render(request,template_name)

def myOrders(request):
    return HttpResponse("<h1>This is my orders </h1>")

def myAccount(request):
    return HttpResponse("<h1>This is My Account </h1>")

def help(request):
    return HttpResponse("<h1>This is help </h1>")

def myCart(request):
    return HttpResponse("<h1>This is my cart</h1>")

def aisles(request):
    return HttpResponse("<h1>This is aisle</h1>")

def login(request):
    return HttpResponse("<h1>This is guest</h1>")

def guest(request):
    return HttpResponse("<h1>This is guest</h1>")

def searchresults(request):
    all_items = Item.objects.all()
    holdoriginal = ""
    html =''

    #   for formatitems in all_items:
    #       holdoriginal = formatitems
    ##   {% for originalitems in holdoriginal %}
    ##        {%  if modelitems in originalitems%}
    ##        {% endfor    %}
    ##
    query = request.GET['q']
    html = str(query)
    context = {'all_items': all_items, 'query': html, 'holdoriginal': holdoriginal}
    if request.method == 'GET' and query != '':
        return render(request, 'index/search_results.html', context)
    else:
        return render(request, 'index/index.html')

        # html = " "
        # query = request.GET['q']


        #    if request.method == 'GET':

        #       for modelitems in all_items:
        #          html += '<a href="" >' + modelitems.item_name + '</a><br>'
        #          if (modelitems.item_name).find(str(query)):
        #              return HttpResponse(html)

        #return HttpResponse(html)
        #return render(request, 'index/index.html')
        #      return render(request, 'index/search_results.html', context)
        #  else:
        #      return render(request, 'index/index.html')



        #return HttpResponse(html)

        # if request.method == 'GET':
        #search_query = request.GET.get('q', None)
        #    return HttpResponse({query})
        #else:
        #   return render(request, 'index/index.html')