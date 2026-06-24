from django.urls import path
from . import views
#Urlpatterns acceso a las urls en lista

#rutas
urlpatterns = [
    path("<int:day>", views.days_week_int),
    path("<str:day>", views.days_week) # Creando vista dinamcia 
]
