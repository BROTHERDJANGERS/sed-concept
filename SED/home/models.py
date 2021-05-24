from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

from django.contrib.postgres.fields import ArrayField



#Комманда для обновления базы 



#./manage.py reset_db | ./manage.py dbshell    



#Таблица с данными о загрзке файла
class add_Doc(models.Model):    
    title = models.CharField('Наименование документа',max_length=150)
    user_upload = models.CharField('Добавил',max_length=150,null=True)
    create_datetime = models.DateTimeField(('Дата добавления'), auto_now=False, auto_now_add=True)
    action_name = models.CharField(("Действие"), max_length=50,default="")
    file_url = models.CharField(("Ссылка на документ"), max_length=50,default="")
    
#Возвращение данных содержимого таблиы
    def __str__(self):
        return self.id
        return self.action_name
        return self.title
        return self.user_upload
        return self.create_datetime
        return self.file_url


class Signature(models.Model):
    
    file = models.ForeignKey(add_Doc,on_delete=models.CASCADE)
    #user_signature = models.CharField('Подписал',max_length=150,null=True)
    user_signature = ArrayField(models.CharField(max_length=200), blank=True),
    date_signature = models.DateField()
    
    def __str__(self):
        return self.file
        return self.user_signature
    
          
    #title = models.ForeignKey(add_Doc,on_delete=models.CASCADE)


   
""" class Task(models.Model):
    ...
    class Meta:
        permissions = [
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        ] """
