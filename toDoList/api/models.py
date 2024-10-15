from django.db import models

class User(models.Model):
    id_user = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    

class Task(models.Model):
    id_task = models.IntegerField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_description = models.CharField(max_length=200)
    task_concludedFlag = models.CharField(max_length=1)