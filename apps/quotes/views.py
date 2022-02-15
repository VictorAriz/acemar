from django.shortcuts import render, redirect
from .models import Quotes
from django.contrib import messages

# Create your views here.


def home(request):
    quotesList = Quotes.objects.all()
    # messages.success(request, '¡Cotizaciones listadas!')
    return render(request, "gestionQuotes.html", {"quotess": quotesList})

def homee(request):
    quotesList = Quotes.objects.all()
    # messages.success(request, '¡Cotizaciones listadas!')
    return render(request, "gestionQuotes2.html", {"quotess": quotesList})


def registrarQuotes(request):
    # codigo = request.POST['txtCodigo']
    name = request.POST['txtName']
    description = request.POST['txtDescription']
    # mail = request.POST['txtMail']
    # user_name = request.POST['txtUser_name']
    # document = request.POST['numDocument']

    quotes = Quotes.objects.create(
        name=name, description=description)
    messages.success(request, '¡Cotizacion registra!')
    return redirect('/home2')

def registrarQuotes2(request):
    # codigo = request.POST['txtCodigo']
    name = request.POST['txtName']
    description = request.POST['txtDescription']
    # mail = request.POST['txtMail']
    # user_name = request.POST['txtUser_name']
    # document = request.POST['numDocument']

    quotes = Quotes.objects.create(
        name=name, description=description)
    messages.success(request, '¡Cotizacion registra!')
    return redirect('/home2e')


# def edicionUser(request, codigo):
def edicionQuotes(request, id):
    quotes = Quotes.objects.get(id=id)
    return render(request, "edicionQuotes.html", {"quotess": quotes})


def editarQuotes(request):
    # codigo = request.POST['txtCodigo']
    name = request.POST['txtName']
    description = request.POST['txtDescription']
    # mail = request.POST['txtMail']
    # user_name = request.POST['txtUser_name']
    # document = request.POST['numDocument']

    quotes = Quotes.objects.get(id=id)
    quotes.name = name
    quotes.description = description
    # user.mail = mail
    # user.user_name = user_name
    # user.document = document
    quotes.save()

    messages.success(request, '¡Cotizacion actualizada!')

    return redirect('/home2')


# def eliminarUser(request, codigo):
def eliminarQuotes(request, id):
    quotes = Quotes().objects.get(id=id)
    quotes.delete()

    messages.success(request, '¡ Cotizacion eliminada!')

    return redirect('/home2')