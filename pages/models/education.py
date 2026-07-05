from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models.utils.standard_models import StandardModel
from django.contrib.auth.models import User


class Education(StandardModel):
    """Classe pour définir les écoles dont j'ai fréquenté """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='educations',
        verbose_name=_('Accueil Page')
    )

    name = models.CharField(max_length=50, verbose_name=_('Nom'))
    ville = models.CharField(max_length=100, verbose_name=_('Ville'))
    diplome = models.CharField(max_length=200,verbose_name=_('Diplôme Obtenue'))
    description = models.TextField(max_length=900,verbose_name=_('Description'))
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"

    def __str__(self):
        return f"{self.name}"