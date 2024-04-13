from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from .models import Bannersection


def Home(request):
    bgimg = Bannersection.objects.filter().order_by('-Id')
    
    return render(request, 'uifiles/home.html',{'bgimg':bgimg})

def Services(request):
    return render(request, 'uifiles/services.html')

def RecentProjects(request):
    return render(request, 'uifiles/projects.html')

def Contact(request):
    return render(request, 'uifiles/Contact.html')
