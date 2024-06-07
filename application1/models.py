from django.db import models
class employees(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=29)
    esal=models.CharField(max_length=30)
    design=models.CharField(max_length=40)


# Create your models here.
