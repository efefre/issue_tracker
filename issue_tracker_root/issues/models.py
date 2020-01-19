from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.TextField(verbose_name=_('Project name'), unique=True)
    slug = models.SlugField(max_length=10)

    def __str__(self):
        return self.name
