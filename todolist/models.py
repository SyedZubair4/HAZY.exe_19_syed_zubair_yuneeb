from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    addtask = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    Duetime = models.DateTimeField()
    userName = models.ForeignKey(User, on_delete=models.CASCADE)

   