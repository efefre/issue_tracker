from django import template
from ..models import Project

register = template.Library()

@register.simple_tag
def projects_list():
    return Project.objects.all().order_by('-created')


@register.filter
def tasks(list):
    tasks_list = []
    for issue in list:
        if issue.type == 'task':
            tasks_list.append(issue)
    return tasks_list


@register.filter
def bugs(list):
    tasks_list = []
    for issue in list:
        if issue.type == 'bug':
            tasks_list.append(issue)
    return tasks_list
