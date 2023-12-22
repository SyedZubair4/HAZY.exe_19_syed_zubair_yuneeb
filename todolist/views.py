from django.shortcuts import render
from .models import Todo
from django.shortcuts import get_object_or_404
import time


# Create your views here.
def Home(request):
    return render(request, 'home.html')

def landingPage(request):
    
    return render(request,'landingPage.html')


def addtask(request):
    if request.method == 'POST':
        datas = Todo()
        datas.adtask=request.POST['addtask']
        datas.description=request.POST['description']
        datas.Duetime=request.POST['duetime']
        datas.save()
    return render(request, 'home.html', {'datas':datas})

def editTask(request, task_id):
    task = get_object_or_404(Todo, pk=task_id)

    if request.method == 'POST':
        # Fetch the updated values from the request
        new_adtask = request.POST.get('adtask', '')
        new_description = request.POST.get('description', '')
        new_duetime = request.POST.get('Duetime', '')

        # Update the task fields with the new values
        task.adtask = new_adtask
        task.description = new_description
        task.Duetime = new_duetime

        # Save the updated task
        task.save()

        # Redirect to the landing page and pass the updated task_id as a parameter
        return render(request,'LandingPage', updated_task_id=task_id)

def deleteTask(request, task_id):
    todoInstance = get_object_or_404(Todo, pk=task_id)
    todoInstance.delete()
    return render(request,'home.html')


def Mode(request,userMode):
    if userMode == 1:
        return render(request,'registerUP.html')
    elif userMode == 2:
        return render(request, 'register.html')   
    else:
        return render(request, 'restricted.html') 

    


    


