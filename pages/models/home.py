from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models.utils.standard_models import StandardModel
from django.contrib.auth.models import User


class Home(StandardModel):
    """Classe pour définir la page d'accueil"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='homes',
        verbose_name=_('Accueil Page')
    )

    name = models.CharField(max_length=50, verbose_name=_('Nom'))
    picture = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        verbose_name = "Accueil"
        verbose_name_plural = "Accueils"

    def __str__(self):
        return f"{self.name}"