from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound # Importar 

# Create your views here.
def days_week_int(request, day):
    pass           
    return HttpResponse(day)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

#Para crear vistas dinamicas 
def days_week(request , day):
    quote_text = None
    if day == "monday":
        quote_text = "Hola Lunes :D"
    elif day == "tuesday":
        quote_text = "Hola Tuesdaday :D" 
    else:
        return HttpResponseNotFound("Day not found")     
    return HttpResponse(quote_text)