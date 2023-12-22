from django.db import models

# Create your models here.
class Todo(models.Model):
    adtask = models.CharField(max_length=255)
    description = models.TextField()
    Duetime = models.DateTimeField()

    def __str__(self):
        return self.adtask

   