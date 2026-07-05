from django.shortcuts import render
from pages.models.education import Education
from django.shortcuts import get_object_or_404
# Create your views here.

def home_pages(request):
    datas = {
                "educations":Education.objects.all()

    }
    return render(request,"resume.html",datas)