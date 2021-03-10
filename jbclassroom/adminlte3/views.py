from django.http import HttpResponseRedirect
from django.shortcuts import render
import sqlite3  #imports sqlite YT
conn=sqlite3.connect("db.sqlite3") 
cursor=conn.cursor() #uses db.sqlite3 as the database
details = []

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if request.POST['isTeacher'] == 'True':
            isTeacher = True
        #NOW WE NEED TO ADD IT TO THE DATABASE
        #find a way to append a different ID each time to details
        details.append(username)
        details.append(email)
        details.append(password) #appends stuff
        details.append(isTeacher)
        cursor.execute ("INSERT INTO adminlte3_users VALUES (?,?,?,?,?)", details)
        conn.commit() #executes and commits inputing the values into the datbase
        details = []
        conn.close() #closes db.sqlite3
    return render(request, 'adminlte/register.html')

#ALSO WE NEED TO CREATE THE LOGIN REQUEST AND CHECK IT WITH THE DATABASE