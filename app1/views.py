from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, "app1/basis.html")

def anmeldung(request):
    return render(request, "app1/anmeldung.html")