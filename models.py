from django.db import models
from datetime import *
from django.core.validators import *
from phonenumber_field.modelfields import *


CHOICES = (
    ("Success","Success"),
    ("faild","faild"),
    ("pending..","pending.."),
)


class parentstudent(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    email=models.EmailField(default="@gmail.com")
    dob = models.DateField(default=date.today)
    time = models.TimeField(default="00:00:00")
    file = models.FileField(upload_to='files/', default='default_file_path') 
    video = models.FileField(upload_to='Vedios/', default='default_video_path')   
    url = models.URLField(default='https://example.com/default_chaptha_url')
    image = models.ImageField(max_length=None, upload_to="image/", default="default_image.jpg")
    phone = PhoneNumberField(null = True, blank = True)


    def __str__(self):
        return self.name
    
class childstudent(models.Model):
    username = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=CHOICES, default='enter')
    frkey = models.ForeignKey(parentstudent,on_delete=models.CASCADE)#CASECADE in replace by many other modules.
    verify = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.username