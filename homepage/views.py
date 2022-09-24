from django.shortcuts import render
from homepage.models import Project

def index(request):
    projects = Project.objects.all()
    context = {"projects" : projects}
    return render(request, "landing_page.html", context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)