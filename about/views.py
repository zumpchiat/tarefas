from django.http import HttpResponse
from django.shortcuts import render


def about(request):
   form = 'qq'
   # return HttpResponse("about page")
   # return render(request, 'about.html', 'form')
   return render(request, 'about.html')
