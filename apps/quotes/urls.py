from django.urls import path
from .import views

urlpatterns = [
    path('home2', views.home),
    path('home2e', views.homee),
    path('registrarQuotes/', views.registrarQuotes),
    path('registrarQuotes2/', views.registrarQuotes2),
    path('edicionQuotes/<id>', views.edicionQuotes),
    path('editarQuotes/', views.editarQuotes),
    path('eliminarQuotes/<id>', views.eliminarQuotes)
]