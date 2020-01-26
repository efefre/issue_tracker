from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
def get_attachment_path(instance, filename):
    return 'uploads/profile/{0}/{1}'.format(instance.username, filename)


class CustomUser(AbstractUser):
    profile_img = models.FileField(upload_to=get_attachment_path, verbose_name=_('Profile image'))

    def __str__(self):
        return self.username
