from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class StandardModel(models.Model):
    
    class Meta :
        
        abstract = True
        
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)