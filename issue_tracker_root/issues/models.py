from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
import pendulum

# Create your models here.
class Project(models.Model):
    name = models.TextField(verbose_name=_('Project name'), unique=True)
    slug = models.SlugField(max_length=10)

    def __str__(self):
        return self.name

class Issue(models.Model):

    ISSUE_TYPE_CHOICES = [
        ('task', 'Task'),
        ('bug', 'Bug')
    ]

    ISSUE_STATUS_CHOICES = [
        ('to do', 'To do'),
        ('in progress', 'In progress'),
        ('done', 'done')
    ]

    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues', verbose_name=_('Project'))
    issue_type = models.CharField(choices=ISSUE_TYPE_CHOICES, default='task', verbose_name=_('Issue type'), max_length=5)
    issue_status = models.CharField(choices=ISSUE_STATUS_CHOICES, default='to do', verbose_name=_('Issue status'),
                                  max_length=20)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='low', verbose_name=_('Issue priority'),
                                  max_length=10)
    assingee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_assignee', verbose_name=_('Assignee'))
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_reporter', verbose_name=_('Reporter'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    summary = models.TextField(verbose_name=_('Summary'), max_length=250)
    description = models.TextField(verbose_name=_('Description'))
    environment = models.TextField(verbose_name=_('Environment'), max_length=100)

    def __str__(self):
        return f'{self.summary} (project: {self.project})'

class Comment(models.Model):
    comment_text = models.TextField(verbose_name=_('Comment'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Author'))
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Issue'))

    def __str__(self):
        return f'Comment from issue {self.issue.summary}'


def get_attachment_path(instance, filename):
    datetime=pendulum.now('Europe/Warsaw')
    datetime = datetime.to_datetime_string().replace(':','_')
    return 'uploads/{0}/{1}-{2}'.format(instance.issue.id, datetime, filename)


class Attachment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='attachments', verbose_name=_('Issue'))
    file = models.FileField(upload_to=get_attachment_path, verbose_name=_('File'))
    added = models.DateTimeField(auto_now_add=True, verbose_name=_('Added'))

    def __str__(self):
        return f'Attachment from issue {self.issue.summary} (id: {self.issue.id}'
