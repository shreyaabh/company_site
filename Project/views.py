from django.shortcuts import render, get_object_or_404
from .models import Project


def project(request):
    projects = Project.objects.order_by("-Date")
    return render(request, "Project/project.html", {"projects": projects})


def detail(request, Project_id):
    projects = get_object_or_404(Project, pk=Project_id)
    return render(request, "Project/detail.html", {"projects": projects})

