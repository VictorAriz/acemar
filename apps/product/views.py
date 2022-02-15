from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages

# Create your views here.


def home(request):
    productList = Product.objects.all()
    # messages.success(request, '¡Productos listados!')
    return render(request, "gestionProduct.html", {"products": productList})


def registrarProduct(request):
    name = request.POST['txtName']
    description= request.POST['txtDescription']
    value= request.POST['numValue']

    product = Product.objects.create(
        name=name, description=description, value=value)
    messages.success(request, '¡Producto registrado!')
    return redirect('/home3')


# def edicionUser(request, codigo):
def edicionProduct(request, id):
    product = Product.objects.get(id=id)
    return render(request, "edicionProduct.html", {"product": product})


def editarProduct(request,id):
    name = request.POST['txtName']
    description = request.POST['txtDescription']
    value = request.POST['numValue']

    product = Product.objects.get(id=id)
    product.name = name
    product.description = description
    product.value = value
    product.save()

    messages.success(request, '¡Producto actualizado!')

    return redirect('/home3')


# def eliminarUser(request, codigo):
def eliminarProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()

    messages.success(request, '¡Producto eliminado!')

    return redirect('/home3')