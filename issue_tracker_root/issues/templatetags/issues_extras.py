from django import template
from ..models import Project

register = template.Library()

@register.simple_tag
def projects_list():
    return Project.objects.all().order_by('-created')
