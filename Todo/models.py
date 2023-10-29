from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image =models.ImageField(upload_to='pics', null=True,default='pics/loginback.png')
    text=models.CharField(max_length=225, null=False,blank=False)
    description=models.TextField(max_length=225, null=True,blank=False)
    done = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text