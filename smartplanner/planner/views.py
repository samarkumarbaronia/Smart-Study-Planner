from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        date = request.POST.get('date')

        Task.objects.create(title=title, subject=subject, date=date)

    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})


def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('/')
