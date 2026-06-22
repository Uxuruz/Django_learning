from django.urls import path
from . import views
#Urlpatterns acceso a las urls en lista

#rutas
urlpatterns = [

    path("<day>", views.days_week) # Creando vista dinamcia 
]
