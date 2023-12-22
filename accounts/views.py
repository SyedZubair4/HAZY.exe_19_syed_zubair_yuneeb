import json
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import time

# Create your views here.

def temporary_page(request):
    return render(request, 'preloaderPage.html')


def created(request):
    return render(request, 'landingPage.html')

def register(request):
    
    # Load data from the JSON file
    json_path = 'static/JsonFiles/package.json'  # Adjust the path accordingly
    with open(json_path, 'r') as json_file:
        package_data = json.load(json_file)

    if request.method == 'POST':
        usn = request.POST['username']
        em = request.POST['email']
        passw = request.POST['password']

        user = User.objects.create_user(username=usn, password=passw, email=em)
        user.save()
        return render(request, 'home.html', {'package_data': package_data})

    return render(request, 'home.html', {'package_data': package_data})


# def register(request):
    
#     if request.method == 'POST':
#         usn=request.POST['username']
#         em=request.POST['email']
#         passw=request.POST['password']

#         user=User.objects.create_user(username=usn,password=passw,email=em)
#         user.save()
#         return render(request, 'register.html', {'package_data': data})

    
#login function
def userLogin(request):
    if request.method == 'POST':
        usn = request.POST['username']
        passw = request.POST['password']

        user = auth.authenticate(username=usn, password=passw)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

# def userLogin(request):
#     if request.method =='POST':
#         usn=request.POST['username']
#         passw=request.POST['password']

#         usern = auth.authenticate(username=usn)
#         userp = auth.authenticate(password=passw)
#         if usern is not None:
#             if userp is not None:
#                 return redirect('/')
#             else:
#                 messages.info('Invalid Password')
        
#         elif userp is not None:
#             if usern is not None:
#                 return redirect('/')
#             else:
#                 messages.info('Invalid Username')
        
#         else:
#             messages.info('Invalid Username and Password')


# def userLogout(request):
#     auth.logout(request)
#     return render(request,'landingPage.html')

        
def userLogout(request):
    auth.logout(request)
    messages.info(request, 'Logout successful.')
    return redirect('/')

       



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

def landingPage(request):
    
    return render(request,'landingPage.html')