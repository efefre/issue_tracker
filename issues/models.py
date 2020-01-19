from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Project(models.Model):
    name = models.TextField(verbose_name=_('Project name'), unique=True)
    slug = models.SlugField(max_length=10)
