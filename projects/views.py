from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def projects(request):
    template = 'projects/projects.html'
    context = {}

    return render(request, template, context)


def project(request, pk):
    template = 'projects/single_project.html'
    context = {'pk': pk}

    return render(request, template, context)
