from django.shortcuts import render
from django.http import HttpResponse # Importamos para poder usar httpresponse
from datetime import date
# Create your views here.
def home(request):
    today = date.today()
    stack = ["Python","Dart","PHP","flutter","Django"]
    return render(request, "landing/landing.html",{
        "name": "Dario",
        "name2": "Elias",
        "today": today,
        "stack": stack
    })