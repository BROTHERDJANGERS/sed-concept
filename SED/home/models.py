from django.db import models
from django.contrib.auth.models import User


#def user_directory_path(instance, filename):    
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
#    return 'user_{0}/{1}'.format(instance.user.id, filename)

""" class Doc(models.Model): # таблица с данныи и о загрузке
    #user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    user_upload = models.CharField(max_length=150,null=True)
    

    #doc = models.FileField(upload_to="docs/")

    def __str__(self):
        return self.title

class Actions_user(models.Model): # таблица с действиями
    action_name = models.CharField(max_length=150)
    time = models.DateField()

    def __str__(self):
        return self.action_name """


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
   