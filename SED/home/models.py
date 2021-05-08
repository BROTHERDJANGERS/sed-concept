from django.db import models
from django.contrib.auth.models import User


#def user_directory_path(instance, filename):    
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
#    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Doc(models.Model):
    #user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    user_upload = models.CharField(max_length=150,null=True)
    #doc = models.FileField(upload_to="docs/")

    def __str__(self):
        return self.title

class Actions_user(models.Model):
    action_name = models.CharField(max_length=150)
    time = models.DateField()

    def __str__(self):
        return self.action_name