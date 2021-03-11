from django.urls import path
from . import views

#THIS IS THE SUBPAGE /a/ WHERE ALL FORMS THAT REQUIRE USER INPUT ARE KEPT. THIS IS SO ITS EASY TO USE views.py AND TAKE USER INPUTS
urlpatterns = [
    path('register/', views.register, name='register'), #runs the function in views.py, which opens the register page and waits for a POST
    path('login/', views.login, name='login'),  #runs the function in views.py, which opens the login page and waits for a POST
    path('meeting/', views.Meeting, name='meeting') #runs the function in views.py, which opens the meeting page and waits for a POST

]