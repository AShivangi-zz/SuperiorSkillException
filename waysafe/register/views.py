from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import  UserRegisterForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)



# Create your views here.
# Create your views here.
def index(request): #always put in request
    template_name = 'index/login.html'
    return render(request , template_name)

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

