from django.shortcuts import render
from pages.models.projects import Project

# Create your views here.
def project_pages(request):
    datas = {
    "projects": Project.objects.all()
    }
    return render(request,"projects.html",datas)