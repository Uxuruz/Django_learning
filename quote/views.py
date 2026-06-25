from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound # Importar 

#Diccionarios dias de la semana

days_of_week = {
    "monday": "Hola monday",
    "tuesday": "hola tuesday",
    "wednesday": "hola wednesday",
    "thursday": "Hola Thursdat",
    "friday": "Helo Friday",
    "saturday": "hola saturday",
    "sunday": "hola sundays",
}

# Create your views here.
def days_week_int(request, day):     
    return HttpResponse(day)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

#Para crear vistas dinamicas 
def days_week(request, day):
    try : #Manejo de errores
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except:
       return HttpResponseNotFound("Day not found")     
    