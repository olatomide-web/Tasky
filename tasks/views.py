from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def tasks_homepage(request):
    task = Tasks.objects.all().order_by('-id')
    context = {
        'task' : task,
    }
    return render(request, 'tasks/homepage.html', context)
    
def tasks_details(request, id=id):
    task = get_object_or_404(Tasks, id=id)
    context = {
        'task' : task,
    }
    return render(request, 'tasks/tasks_details.html', context)

def tasks_delete(request, id=id):
    task = get_object_or_404(Tasks, id=id)
    task.delete()
    return redirect('tasks-homepage')

def tasks_update(request, id):
    task = get_object_or_404(Tasks, id=id)
    form = UpdateTask(request.POST or None, instance=task)
    if request.method == "POST":
        form = UpdateTask(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks-homepage')
        else:
            form = UpdateTask(request.POST)
        pass
    else:
        form = UpdateTask(request.POST)
    context = {
        'form' : form,
    }
    return render(request,'tasks/tasks_update.html', context)


def tasks_create(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks-homepage')
        else:
            form = CreateTask()
    else:
        form = CreateTask()
    context = {
        'form' : form,
    }
    return render(request, 'tasks/tasks_create.html', context)

def tasks_search(request):
    task = Tasks.objects.order_by('-id')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            task = task.filter(Task_name__icontains=keyword)

    context = {
        'task' : task,
    }
    return render(request,'tasks/tasks_search.html', context)
