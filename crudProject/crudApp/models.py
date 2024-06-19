from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="image") #pip install pillow


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    