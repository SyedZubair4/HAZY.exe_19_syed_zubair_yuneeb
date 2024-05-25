from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.decorators import login_required


# Create your views here.
def Home(request):
    return render(request, 'home.html')

def landingPage(request):
    
    return render(request,'landingPage.html')


# addding task function
@login_required
def addtask(request):
    if request.method == 'POST':
        UserName=request.user
        datas = Todo()
        datas.addtask=request.POST['addtask']
        datas.description=request.POST['description']
        datas.Duetime=request.POST['duetime']
        datas.userName=UserName
        datas.save()
        dataToSend = Todo.objects.filter(userName=UserName)
        return render(request, 'home.html', {'username':UserName.username,'datas':dataToSend})
    else:
        return redirect('/')


# deleting task function
@login_required
def deleteTask(request):
    if request.method == "POST":
        desCription=request.POST.get('description')
        UserName=request.user
        task_to_remove = Todo.objects.filter(description=desCription,userName=UserName)
        task_to_remove.delete()
    UserName=request.user
    dataToSend = Todo.objects.filter(userName=UserName)
    return render(request,'home.html', {'username':UserName.username,'datas':dataToSend})



# editing task function
@login_required
def editTask(request, task_id):
    task = get_object_or_404(Todo, pk=task_id)

    if request.method == 'POST':
        userName=request.user.username
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





