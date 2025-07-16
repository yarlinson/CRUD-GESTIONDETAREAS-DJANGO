from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_Task, name='home'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/create/', views.create_Task, name='create_Task'),
    path('tasks/', views.listTasks, name='task'),
    path('tasks/detaill/<int:task_id>', views.task_detaill, name='task_detaill'),
    path('tasks/<int:task_id>/completed', views.task_complete, name='task_complete'),
    path('tasks/<int:task_id>/deleted', views.task_delete, name='task_delete')
] 