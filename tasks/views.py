from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('IOIO')


def tasklist(request):
    return render(request, "tasks/list.html")


def your_name(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
