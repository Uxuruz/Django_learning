from django.shortcuts import render
from django.http import HttpResponse # Importamos para poder usar httpresponse
from datetime import date
# Create your views here.
def home(request):
    today = date.today()
    stack = [
        {'id': 'python', 'name': "Python"},
        {'id': 'dart', 'name': "Dart"},
        {'id': 'php', 'name': "PHP"},
        {'id': 'flutter', 'name': "Flutter"},
        {'id': 'django', 'name': "Django"}
    ]
    return render(request, "landing/landing.html",{
        "name": "Dario",
        "name2": "Elias",
        "today": today,
        "stack": stack
    })

def stack_details(request, tool):  
  return HttpResponse(f"Tecnologia {tool}") 