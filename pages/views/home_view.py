from django.shortcuts import render
from pages.models.home import Home
from django.shortcuts import get_object_or_404
# Create your views here.

def home_pages(request):
    homes = Home.objects.filter(active=True)
    datas = {
    }
    return render(request,"index.html",datas)