from django.contrib import admin
from pages.models.home import Home
from pages.models.resume import Resume
from pages.models.projects import Project

# Register your models here.
admin.site.register(Home)
admin.site.register(Resume)
admin.site.register(Project)