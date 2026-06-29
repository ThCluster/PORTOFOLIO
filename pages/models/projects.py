from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models.utils.standard_models import StandardModel
from django.contrib.auth.models import User
# Create your models here.

class Project(StandardModel):
    
    """ Classe pour definir page qui definir mes projets"""
    
    class Meta :
        
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        
    User = models.ForeignKey(User, on_delete=models.CASCADE,related_name='projects',verbose_name=_('Utilisateur'))
    name_project = models.CharField(max_length=50,blank=True,null=True,verbose_name=_('Nom du Projet'))
    description = models.TextField(max_length=500,blank=True,null=True,verbose_name=_('Description du Projet'))
    picture = models.ImageField(upload_to='media/',blank=True,null=True,verbose_name=_('Image projet'))
    
def __str__(self):
    return f"{self.name_projet}"
        
    
