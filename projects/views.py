from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


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


def createProjects(request):

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('projects')

    form = ProjectForm()

    template = 'projects/project_form.html'
    context = {'form': form}

    return render(request, template, context)


def updateProject(request, pk):

    project_instance = Project.objects.get(id=pk)
    form = ProjectForm(instance=project_instance)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES,instance=project_instance)
        if form.is_valid:
            form.save()
            return redirect('projects')

    template = 'projects/project_form.html'
    context = {'form': form}

    return render(request, template, context)


def deleteProject(request, pk):

    project_instance = Project.objects.get(id=pk)

    if request.method == "POST":
        project_instance.delete()
        return redirect('projects')

    template = 'projects/delete_project.html'
    context = {'project': project_instance}

    return render(request, template, context)