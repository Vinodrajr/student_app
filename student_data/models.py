from django.db import models

class Student(models.Model):
    name=models.TextField(max_length=100)
    age=models.IntegerField()
    address=models.TextField(max_length=100)
    phone=models.TextField(max_length=10)

