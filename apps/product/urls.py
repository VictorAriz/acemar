from django.urls import path
from .import views

urlpatterns = [
    path('home3', views.home),
    path('registrarProduct/', views.registrarProduct),
    path('edicionProduct/<id>', views.edicionProduct),
    path('editarProduct/', views.editarProduct),
    path('eliminarProduct/<id>', views.eliminarProduct)
]