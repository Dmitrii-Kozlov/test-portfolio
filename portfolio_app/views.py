from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio_app/index.html', context)