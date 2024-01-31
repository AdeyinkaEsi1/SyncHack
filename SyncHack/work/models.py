from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    pword = models.CharField(max_length=50)

    class Meta:
        unique_together = ('fname', 'lname')


    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.email

