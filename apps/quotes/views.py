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
    document = request.POST['numDocument']
    phone = request.POST['numPhone']
    mail = request.POST['txtMail']
    typematerial = request.POST['txtTypematerial']
    description = request.POST['txtDescription']


    quotes = Quotes.objects.create(
        name=name, document=document, phone=phone, mail=mail, typematerial=typematerial, description=description)
    messages.success(request, '¡Cotizacion registra!')
    return redirect('/home2')

def registrarQuotes2(request):
    # codigo = request.POST['txtCodigo']
    name = request.POST['txtName']
    document = request.POST['numDocument']
    phone = request.POST['numPhone']
    mail = request.POST['txtMail']
    typematerial = request.POST['txtTypematerial']
    description = request.POST['txtDescription']

    quotes = Quotes.objects.create(
        name=name, document=document, phone=phone, mail=mail, typematerial=typematerial, description=description)
    messages.success(request, '¡Cotizacion registra!')
    return redirect('/home2e')


# def edicionUser(request, codigo):
def edicionQuotes(request, id):
    quotes = Quotes.objects.get(id=id)
    return render(request, "edicionQuotes.html", {"quotess": quotes})


def editarQuotes(request):
    # codigo = request.POST['txtCodigo']
    name = request.POST['txtName']
    document = request.POST['numDocument']
    phone = request.POST['numPhone']
    mail = request.POST['txtMail']
    typematerial = request.POST['txtTypematerial']
    description = request.POST['txtDescription']

    quotes = Quotes.objects.get(id=id)
    quotes.name = name
    quotes.document = document
    quotes.phone = phone
    quotes.mail = mail
    quotes.typematerial = typematerial
    quotes.description = description

    quotes.save()

    messages.success(request, '¡Cotizacion actualizada!')

    return redirect('/home2')


# def eliminarUser(request, codigo):
def eliminarQuotes(request, id):
    quotes = Quotes().objects.get(id=id)
    quotes.delete()

    messages.success(request, '¡ Cotizacion eliminada!')

    return redirect('/home2')