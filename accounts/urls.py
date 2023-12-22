from django.urls import path
from . import views

urls=[
    
]

urlpatterns=[
  path('register',views.register,name='register'),
  path('userLogin',views.userLogin,name='login'),
  path('userLogout',views.userLogout,name='logout'),
  path('doneCreating',views.created,name='UserCreated'),
   path('addtask',views.addtask,name='Addtask'),
    path('',views.landingPage,name='LandingPage'),
    path('deleteTask/<int:task_id>/', views.deleteTask, name='delete_task'),
    path('editTask/<int:task_id>/',views.editTask,name='EditTask'),
    
    
  
]
