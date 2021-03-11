"""django_adminlte3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
 


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='adminlte/index.html')),
    #url(r'^login/$', TemplateView.as_view(template_name='adminlte/login.html')),
    #url(r'^register/$', TemplateView.as_view(template_name='adminlte/register.html')),
    url(r'^exampleclass/$', TemplateView.as_view(template_name='adminlte/classes.html')),
    url(r'^teacherdashboard/$', TemplateView.as_view(template_name='adminlte/teachers.html')),
    url(r'^studentdashboard/$', TemplateView.as_view(template_name='adminlte/student_dashboard.html')),
    path('admin/', admin.site.urls), #this is for the admin side of the website, ignore this.
    path('a/', include('adminlte3.urls')), #THIS LINKS TO THE OTHER urls.py FILE MEANT FOR PAGES WHICH REQUIRE USER INPUT AND DATABASE LOOKUPS
]
