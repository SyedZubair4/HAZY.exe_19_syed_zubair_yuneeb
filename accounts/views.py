import json
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from todolist.models import Todo
from django.contrib.auth.decorators import login_required

# navigate to register page
def redirectToRegister(request):
     # Load data from the JSON file
    json_path = 'static/JsonFiles/package.json'  # Adjust the path accordingly
    with open(json_path, 'r') as json_file:
        package_data = json.load(json_file)

    return render(request,'register.html',{'package_data': package_data})

# navigate to login page
def redirectToLogin(request):

    json_path = 'static/JsonFiles/package.json'  # Adjust the path accordingly
    with open(json_path, 'r') as json_file:
        package_data = json.load(json_file)

    return render(request, 'LogIn.html',{'package_data': package_data})

# register function
def register(request):
    if request.method == 'POST':
        usn = request.POST['username']
        em = request.POST['email']
        passw = request.POST['password']

         # Check if username already exists
        if User.objects.filter(username=usn).exists():
            # Handle the case when the username already exists (e.g., display an error message)
            return render(request, 'LogIn.html', {'error_message': 'Username already exists.'})

        user = User.objects.create_user(username=usn, password=passw, email=em)
        user.save()
        userName=usn
        return render(request, 'home.html',{'username':userName})

    return render(request, 'home.html')


    
#login function
def Login(request):
    if request.method == 'POST':
        usn = request.POST['username']
        passw = request.POST['password']

        user = auth.authenticate(username=usn, password=passw)
        userName=usn
        if user is not None:
            auth.login(request, user)

            #fetching the username from the server after login
            @login_required
            def fetchUserName(request):
                user_name=request.user
                return user_name
            
            UserName=fetchUserName(request)
            messages.success(request, 'Login successful.')
            dataToSend= Todo.objects.filter(userName=UserName)
            return render(request,'home.html',{'username':userName,'datas':dataToSend})
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


# logout function
def Logout(request):
    auth.logout(request)
    messages.info(request, 'Logout successful.')
    return render(request,'landingPage.html')

# first page to show
def landingPage(request):
    
    return render(request,'landingPage.html')