from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.


def home(request):
    userList = User.objects.all()
    # messages.success(request, '¡Usuarios listados!')
    return render(request, "gestionUser.html", {"users": userList})


def registrarUser(request):
    name = request.POST['txtName']
    last_name= request.POST['txtLast_name']
    document = request.POST['numDocument']
    phone = request.POST['numPhone']
    mail = request.POST['txtMail']
    address = request.POST['txtAddress']
    city = request.POST['txtCity']
    state_province = request.POST['txtState_province']
    country = request.POST['txtCountry']
    website = request.POST['txtWebsite']
    user_name = request.POST['txtUser_name']


    user = User.objects.create(
        name=name, last_name=last_name, document=document, phone=phone, mail=mail, address=address, city=city, state_province=state_province, country=country, website=website, user_name=user_name)
    messages.success(request, '¡Usuario registrado!')
    return redirect('/home')


# def edicionUser(request, codigo):
def edicionUser(request, id):
    user = User.objects.get(id=id)
    return render(request, "edicionUser.html", {"user": user})


def editarUser(request, id):
    # codigo = request.POST['txtCodigo']
    name = request.POST['txtName']
    last_name= request.POST['txtLast_name']
    document = request.POST['numDocument']
    phone = request.POST['numPhone']
    mail = request.POST['txtMail']
    address = request.POST['txtAddress']
    city = request.POST['txtCity']
    state_province = request.POST['txtState_province']
    country = request.POST['txtCountry']
    website = request.POST['txtWebsite']
    user_name = request.POST['txtUser_name']

    user = User.objects.get(id=id)
    user.name = name
    user.last_name = last_name
    user.document = document
    user.phone = phone
    user.mail = mail
    user.address = address
    user.city = city
    user.state_province = state_province
    user.country = country
    user.website = website
    user.user_name = user_name

    user.save()

    messages.success(request, '¡Usuario actualizado!')

    return redirect('/home')


# def eliminarUser(request, codigo):
def eliminarUser(request, id):
    user = User.objects.get(id=id)
    user.delete()

    messages.success(request, '¡Usuario eliminado!')

    return redirect('/home')







