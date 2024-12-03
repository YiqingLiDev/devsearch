from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.

def projects(request):

    projects = Project.objects.all()

    template = 'projects/projects.html'
    context = {'projects': projects}

    return render(request, template, context)


def project(request, pk):

    projectobj = Project.objects.get(id=pk)

    template = 'projects/single_project.html'
    context = {'pk': pk, 'project': projectobj}


    return render(request, template, context)
