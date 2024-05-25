from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns=[
    path('addtask',views.addtask,name='Addtask'),
    path('',views.landingPage,name='LandingPage'),
    path('deleteTask', views.deleteTask, name='delete_task'),
    path('editTask',views.editTask,name='EditTask'),   
]