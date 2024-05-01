from django.db import models

# Create your models here.


class Movies(models.Model):
    Name=models.CharField(max_length=100)
    Details =models.CharField(max_length=200)
    def __str__(self):
        return self.Name



class Student(models.Model):
    Name= models.CharField(max_length=100)
    Class= models.CharField(max_length=20)
    Subject= models.CharField(max_length=60)
    def __str__(self):
        return self.Name

