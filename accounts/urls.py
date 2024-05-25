from django.urls import path, include
from . import views


urlpatterns=[
  path('register',views.register,name='register'),
  path('redirectToRegister',views.redirectToRegister,name='redirectToRegister'),
  path('redirectToLogin',views.redirectToLogin,name='redirectToLogin'),
  path('Login',views.Login,name='Login'),
  path('Logout',views.Logout,name='Logout'),
  path('',views.landingPage,name='LandingPage'),
  path('accounts/addtask',include('todolist.urls'))
]
