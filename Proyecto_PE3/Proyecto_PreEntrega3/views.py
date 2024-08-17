from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def funcion(req):
    return HttpResponse("Vamos bien")