from django.shortcuts import render
from pages.models.resume import Resume

# Create your views here.
def resume_pages(request):
    datas = {
        "resume":Resume.objects.all()
    }
    return render(request,"resume.html",datas)