from django.http import HttpResponseRedirect
from django.shortcuts import render

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if request.POST['isTeacher'] == 'True':
            isTeacher = True


    return render(request, 'adminlte/register.html')
