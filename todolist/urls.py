from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns=[
    path('addtask',views.addtask,name='Addtask'),
    path('',views.landingPage,name='LandingPage'),
    path('deleteTask/<int:task_id>/', views.deleteTask, name='delete_task'),
    path('editTask/<int:task_id>/',views.editTask,name='EditTask'),
    path('mode/<int:userMode>/',views.Mode,name='MODE'),
    path('home',views.Home, name='Home'),
    
    
]