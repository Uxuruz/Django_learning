from django.shortcuts import render
from django.http import HttpResponse # Importamos para poder usar httpresponse
from datetime import date
# Create your views here.
def home(request):
    today = date.today()
    return render(request, "landing/landing.html",{
        "name": "Dario Castro",
        "name2": "Elias",
        "today": today
    })