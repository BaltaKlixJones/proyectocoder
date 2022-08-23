from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Familia, Momento
from django.template import loader
import datetime

# Create your views here.
def dia_de_hoy(request):
    respuesta = '<h1 style="background-color: rgb(167, 245, 169) ;display: flexbox; color: rgb(0, 1, 1); position: relative; top: 400px; left: 550px; font-size: 40px;border: dotted; width: max-content;"> Hoy es: {0}</h1>'.format(datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S'))
    return HttpResponse(respuesta)


def mama(request):

    mama= Familia(nombre="Patricia", apellido="Jones", edad= 52)
    mama.save()
    texto= f"{mama.nombre} {mama.apellido}, {mama.edad} anios"
    return HttpResponse(texto)

def papa(request):

    papa= Familia(nombre="Ricardo", apellido="Klix", edad= 55)
    papa.save()
    texto= f"{papa.nombre} {papa.apellido}, {papa.edad} anios"
    return HttpResponse(texto)

def hermanomayor(request):

    hermanomayor= Familia(nombre="Santiago", apellido="Klix Jones", edad= 25)
    hermanomayor.save()
    texto= f"{hermanomayor.nombre} {hermanomayor.apellido}, {hermanomayor.edad} anios"
    return HttpResponse(texto)

def hermanomenor(request):

    hermanomenor= Familia(nombre="Juan", apellido="Guinazu", edad= 7)
    hermanomenor.save()
    texto= f"{hermanomenor.nombre} {hermanomenor.apellido}, {hermanomenor.edad} anios"
    return HttpResponse(texto)


def probando_html(request):
    nombre= 'Baltasar'
    apellido= 'Klix Jones'
    lista_familiares = ['Patricia', 'Ricardo', 'Santiago', 'Juan']
    dic = {'nombre': nombre , 'apellido':apellido, 'lista_familiares': lista_familiares}

    plantilla = loader.get_template('template1.html') # Los datos que mi plantilla necesita para mostrar
    documento = plantilla.render(dic)  # Para porcesar y mostrar el archivo final

    return HttpResponse(documento)