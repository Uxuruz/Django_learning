from django.urls import path
from . import views # . porque se encuentra en el mismo directorio y enlazamos views con home

urlpatterns = [
    path('home', views.home , name="home")
]
