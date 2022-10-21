import http
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('IOIO')


def tasklist(request):
   return render(request, "tasks/list.html")
  # return HttpResponse('IOIO')

def nomeseu(request, name):
    return render(request, 'tasks/nomeseu.html', {'name': name})