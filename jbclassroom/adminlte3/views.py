from django.http import HttpResponseRedirect
from django.shortcuts import render
import sqlite3  #imports sql 
import random


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        isTeacher = False
        try:
            request.POST['isTeacher']
            if request.POST['isTeacher'] == 'True':
                isTeacher = True
        except:
            isTeacher = False

        conn=sqlite3.connect("db.sqlite3") 
        cursor=conn.cursor() #uses db.sqlite3 as the database
        details = []
        #NOW WE NEED TO ADD IT TO THE DATABASE
        #find a way to append a different ID each time to details
        #DO LOOKUP FOR LAST ID
        #append last id 
        cursor.execute("SELECT COUNT(*) FROM adminlte3_users")
        number = cursor.fetchone()[0] #Fetches the number of fields of the table
        idS = int(number) + 1 #adds one to the number of fields to append as the primary key
        details.append(idS)
        details.append(username)
        details.append(email)
        details.append(password) 
        details.append(isTeacher)#appends record into array
        cursor.execute ("INSERT INTO adminlte3_users VALUES (?,?,?,?,?)", details) #inserts array into database
        conn.commit() #executes and commits inputing the values into the datbase
        details = []
        conn.close() #closes db.sqlite3
        return render(request, 'adminlte/index.html') #if login works then send back to index page
    return render(request, 'adminlte/register.html')


def login(request):
    if request.method == 'POST':# if this is a POST request we need to process the form data
        email = request.POST['email']
        password = request.POST['password']
        conn=sqlite3.connect("db.sqlite3") 
        cursor=conn.cursor() #uses db.sqlite3 as the database
        cursor.execute("SELECT email FROM adminlte3_users WHERE email = ?", (email,))
        print(cursor.fetchall)
        if cursor.fetchall== email:
            cursor.execute("SELECT password FROM adminlte3_users WHERE email = ?",(email,))
            if cursor.fetchall== password:
                pass
                
                #RIGHT HERE LOOK OVER HERE!!!!!!
                #This is where we would (if we had time) assign a token to a user so they can only see the classes/pages they are in... BUT we ran out of time and trying to complete this would not have been possible.
        conn.close() #closes db.sqlite3

        
    return render(request, 'adminlte/login.html')



def Meeting(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        meetingStart = request.POST['meetingstart']
        meetingEnd = request.POST['meetingend']
        className = request.POST['class']
        conn=sqlite3.connect("db.sqlite3") 
        cursor=conn.cursor() #uses db.sqlite3 as the database
        details = []
        
        details.append(meetingStart)
        details.append(meetingEnd)
        details.append(classId) #appends stuff
        cursor.execute ("INSERT INTO adminlte3_users VALUES (?,?,?,?)", details)
        conn.commit() #executes and commits inputing the values into the datbase
        details = []
        conn.close() #closes db.sqlite3
        return render(request, 'adminlte/index.html') #if login works then send back to index page

    return render(request, 'adminlte/zoom.html')