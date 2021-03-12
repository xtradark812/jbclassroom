from django.db import models

# Create your models here.

class Users(models.Model): #Creates the table to store user records
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    isTeacher = models.BooleanField(default=False)

class Classes(models.Model): #Creates the table to store class records
    auto_increment_id = models.AutoField(primary_key=True)
    className = models.CharField(max_length=64)

class StudentsInClass(models.Model): #Links the student and class tables to show which students are in which class
    auto_increment_id = models.AutoField(primary_key=True)
    classId = models.ForeignKey(Classes,on_delete=models.CASCADE)
    studentId = models.ForeignKey(Users,on_delete=models.CASCADE)

class ZoomMeeting(models.Model): #Creates the table to store all scheduled zoom meetings
    auto_increment_id = models.AutoField(primary_key=True)
    meetingStart = models.DateTimeField()
    meetingEnd = models.DateTimeField()
    classId = models.ForeignKey(Classes,on_delete=models.CASCADE)
