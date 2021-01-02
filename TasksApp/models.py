from django.db import models

class Bucket(models.Model):
    name = models.CharField(max_length=150,unique=True)

class Task(models.Model):
    bucket = models.ForeignKey(Bucket,default=None,null=True,blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    is_done = models.BooleanField(default=False)
    
