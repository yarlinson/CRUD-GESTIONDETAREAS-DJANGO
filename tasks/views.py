from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .forms import RegistroForm, LoginForm, FormCreateTask
from .models import Task
from django.contrib.auth.decorators import login_required

def registro_view(request):
    if request.method == 'POST':
        
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # encripta contraseña
            print(request.POST)
            user.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(request, username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_Task(request):
    if request.method == 'POST':
        try:    
            form = FormCreateTask(request.POST) 
            new_task = form.save(commit=False)
            new_task.user = request.user
            print(new_task)
            new_task.save()
            tasks = Task.objects.filter(user = request.user)
            return render(request, 'create_task.html', {'form': FormCreateTask,'tasks': tasks})
        except ValueError:
            tasks = Task.objects.filter(user = request.user)
            return render(request, 'create_task.html', {'form': FormCreateTask, 'error': 'Please provide valida data','tasks': tasks})
    else:
        tasks = Task.objects.filter(user = request.user)
        return render(request, 'create_task.html', {'form': FormCreateTask,'tasks': tasks})

@login_required
def listTasks(request):
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull=True)
    return render(request, 'task.html', {'tasks': tasks}) 

@login_required
def task_detaill(request, task_id):
    if request.method == "GET": 
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = FormCreateTask(instance=task)
        return render(request,'task_detaill.html', {'task':task, 'form': form})
    else:
        task = get_object_or_404(Task, pk=task_id)
        form = FormCreateTask(request.POST, instance=task)
        form.save()
        return redirect('task')

@login_required        
def task_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        if task.datecompleted:
            # Si la tarea ya está completada, la descompletamos
            task.datecompleted = None
        else:
            # Si la tarea no está completada, la completamos
            task.datecompleted = timezone.now()
        task.save()
        return redirect('create_Task')

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('create_Task')

def home(request):  
    return render(request, 'home.html')