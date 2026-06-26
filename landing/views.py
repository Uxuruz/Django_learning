from django.shortcuts import render
from django.http import HttpResponse # Importamos para poder usar httpresponse

# Create your views here.
def home(request):
    return HttpResponse("Funciona")