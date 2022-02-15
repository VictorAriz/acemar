from django.urls import path
from .import views

urlpatterns = [
    path('home', views.home),
    path('registrarUser/', views.registrarUser),
    path('edicionUser/<id>', views.edicionUser),
    path('editarUser/', views.editarUser),
    path('eliminarUser/<id>', views.eliminarUser)
]