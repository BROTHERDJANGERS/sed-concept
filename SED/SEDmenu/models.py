from django.db import models

# Create your models here.


class Doc(models.Model):
    title = models.CharField(max_length=150)
    doc = models.FileField(upload_to='docs/')

    def __str__(self):
        return self.title