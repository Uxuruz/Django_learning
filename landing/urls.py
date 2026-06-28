from django.urls import path
from . import views # . porque se encuentra en el mismo directorio y enlazamos views con home

urlpatterns = [
    path('home', views.home , name="home"),
    path('stack/<str:tool>', views.stack_details, name = "stack" ) #vita stack que sea string y utiliza variable tool
]
