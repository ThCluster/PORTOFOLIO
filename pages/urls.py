from django.urls import path
from pages.views.home_view import home_pages
from pages.views.resume_view import resume_pages
from pages.views.projects_view import project_pages
# from pages.views.single_projects_view import single_projects_pages

urlpatterns = [
   path('', home_pages, name='home_pages'),
   path('resume/', resume_pages, name='resume_pages'),
   path('projects/', project_pages, name='project_pages'),
#    path('projects/<int:pk>/', single_projects_pages, name='single_projects_pages'),
]
