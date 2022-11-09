from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.tasklist, name='tasklist'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('changestatus/<int:id>', views.changestatus, name="change-status"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('your_name/<str:name>', views.your_name, name='your_name')
]
