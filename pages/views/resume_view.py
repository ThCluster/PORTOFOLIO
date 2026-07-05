from django.shortcuts import render
from pages.models.resume import Resume
from pages.models.education import Education

def resume_pages(request):
    datas = {
        "resumes": Resume.objects.filter(active=True),
        "educations": Education.objects.all(),
    }
    return render(request, "resume.html", datas)