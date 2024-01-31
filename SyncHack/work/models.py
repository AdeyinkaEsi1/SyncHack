# from django.contrib.auth.models import AbstractUser, Group
from django.db import models



class Employee(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    pword = models.CharField(max_length=50)

    class Meta:
        unique_together = ('fname', 'lname')


    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.email

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('incomplete', 'Incomplete'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name