from django.shortcuts import render
from django.http import HttpResponse
from aisle.models import Item
from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from .forms import UserLoginForm, UserRegisterForm

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

def register(request):
    template_name="index/register.html"
    return render(request, template_name)

#
#def login(request):

#    template_name='index/login.html'
#    return render(request,template_name)
#11/4def login(request):
#        form = UserForm(request.POST or None)
#        if form.is_valid():
#            user = form.save(commit=False)
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password']
#            user.set_password(password)
#            user.save()
#            user = authenticate(username=username, password=password)
#            if user is not None:
#                if user.is_active:
#                    login(request, user)
#                    template_name = 'index/index.html'
#                    return render(request, template_name)
#        context = {
#            "form": form,
#        }
#        return render(request, 'index/login.html', context)

def login_view(request):
    title="Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        #redirect
        return redirect("/aisle")

    return render(request, "index/login.html", {"form":form, "title": title})


def register_view(request):
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, user)
        return redirect("/aisle")

    context ={
        "form": form,
        "title": title,
    }
    return render(request, "index/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/index")


def guest(request):
    template_name = 'aisle/index.html'
    return render(request, template_name)

def searchresults(request):
    all_items = Item.objects.all()
    flagcheck = False
    html =''
    captureword = ''

    #   for formatitems in all_items:
    #       holdoriginal = formatitems
    ##   {% for originalitems in holdoriginal %}
    ##        {%  if modelitems in originalitems%}
    ##        {% endfor    %}
    ##



    query = request.GET['q']
    html = str(query)
    if request.method == 'GET' and query != '':
        for modelitems in all_items:
            if str(query) in (modelitems.item_name).lower():
                flagcheck = True
                captureword = modelitems.item_name

        if (flagcheck):
            context = {'all_items': all_items, 'flagcheck': flagcheck, 'itemname': captureword}
            return render(request, 'index/search_results.html', context)
        else:
            newcontext = {'all_items': all_items, 'query': html, 'flagcheck': flagcheck}
            return render(request, 'index/search_results.html', newcontext)

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

