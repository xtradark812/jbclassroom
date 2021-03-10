from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    isTeacher = models.BooleanField(default=False)

