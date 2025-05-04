from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.




def get_tasks(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, "view-task.html", {"tasks": tasks})


def task(request):
    return render(request, "add-task.html") 




def add_task(request):
    if request.method == "POST":
        task = request.POST.get("task")
        description = request.POST.get("description")
        print(task)
        print(description)
        new_task = Task(name=task, description=description)
        new_task.save(force_insert=True)
        return HttpResponse("success") 
    


def delete_task(request, id):
    task = Task.objects.get(id) 
    task.delete()
    return HttpResponse("success")

def hassan(request):
    return HttpResponse("<h1> WELCOME HASSAN</h1>")

# def task(request):
#     return HttpResponse("Later on we'll return tasks")







