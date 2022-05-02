from django.shortcuts import render
from .models import Person, Project
# Create your views here.

def profile(response):
    person = Person.objects.get(id='01')
    context = {'ps': person}
    return render(response, "dashboard/dashboard.html", context)

def biography(response):
    return render(response, "dashboard/biography.html", {})

def skills(response):
    return render(response, "dashboard/skills.html", {})

def projects(response):
    projects = Project.objects.get(id='01')
    context = {'proj': projects, 'ran': range(10)}
    return render(response, "dashboard/projects.html", context)

def contact(response):
    return render(response, "dashboard/contact.html", {})
