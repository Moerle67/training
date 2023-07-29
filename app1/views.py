from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *

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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse(rtn_name))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnmeldeForm()
        print(form)

    return render(request, "app1/forms.html", {"form": form})