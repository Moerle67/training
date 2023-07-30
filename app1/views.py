from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
            messages.success(request, 'Login erfolgreich')
            return redirect(rtn_name)
        # If the user is not authenticated, display an error message and redirect to the home page
        else:
            messages.error(request, 'Name/Passwort falsch')
            data = {
                'name': username,
                'password': password,
            }
            form = AnmeldeForm(data)
            return render(request, "app1/forms.html", {"form": form})

        #return HttpResponseRedirect(reverse(rtn_name))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnmeldeForm()
        return render(request, "app1/forms.html", {"form": form})

def abmeldung(request, rtn_name):
    logout(request)
    messages.success(request, 'Logout erfolgreich')
    return redirect(rtn_name)

def newpwd(request, rtn_name):
    if request.method == "POST":
     # create a form instance and populate it with data from the request:
        form = New_pwdForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            error = False
            pwd_old = request.POST['pwd_old']
            pwd_new1 = request.POST['pwd_new1']
            pwf_new2 = request.POST['pwd_new2']
            if pwd_new1 != pwf_new2:
                messages.error(request, "Passwörter stimmen nicht überein")
                error = True
            if not request.user.check_password(pwd_old):
                messages.error(request, "Altes Passwort ist falsch")    
    else:
        form = New_pwdForm()
        return render(request, "app1/forms.html", {"form": form})
            
           # return render(request, "app1/forms.html", {"form": form})

           
    return redirect(rtn_name)