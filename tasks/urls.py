from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.tasklist, name='tasklist'),
    path('your_name/<str:name>', views.your_name, name='your_name')
]
