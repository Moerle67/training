from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def start(request):
    return render(request, "app1/basis.html")

def anmeldung(request, rtn_name):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AnmeldeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = request.POST['name']
            password = request.POST['password']

        # Authenticate the user with the given username and password
            user = authenticate(username=username, password=password)

        # If the user is authenticated, log them in and redirect to the home page
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect(rtn_name)
        # If the user is not authenticated, display an error message and redirect to the home page
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect(rtn_name)            
        #return HttpResponseRedirect(reverse(rtn_name))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnmeldeForm()
        print(form)

    return render(request, "app1/forms.html", {"form": form})