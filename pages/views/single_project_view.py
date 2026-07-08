from django.shortcuts import render, get_object_or_404
from pages.models.projects import Project

# Create your views here.
def project_detail_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    datas = {
        "project": project
    }
    return render(request, "post-single-projects.html", datas)