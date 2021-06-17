from django.db import models

# Create your models here.
class studnt(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=24)


class master(models.Model):
    sname = models.CharField(max_length=24)
Brach is upda
B
B

C
C
C
    sno = models.IntegerField()
