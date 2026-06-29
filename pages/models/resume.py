from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models.utils.standard_models import StandardModel
from django.contrib.auth.models import User
# Create your models here.

class Resume(StandardModel):
    
    """ Classe pour definir page qui definir mon résumé"""
    
    class Meta :
        
        verbose_name = "Résumé"
        verbose_name_plural = "Résumés"
        
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes',verbose_name=_('Experiences'))
    profession = models.CharField(max_length=50,blank=True,null=True,verbose_name=_('Profession '))
    nom_societe = models.CharField(max_length=100,blank=True,null=True,verbose_name=_('Nom de la société'))
    mission = models.TextField(max_length=500,blank=True,null=True,verbose_name=_('Mission au sein de la société'))
    
def __str__(self):
    return self.profession.user
        
    
