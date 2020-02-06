from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator
import pendulum


# Create your models here.
class Project(models.Model):
    PROJECT_STATUS_CHOICES = [
        ('in progress', 'In progress'),
        ('success', 'success'),
        ('cancel', 'cancel')
    ]

    only_letters = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')

    name = models.TextField(verbose_name=_('Project name'), unique=True)
    slug = models.SlugField(max_length=10, validators=[only_letters])
    status = models.CharField(choices=PROJECT_STATUS_CHOICES,
                              default='in progress',
                              verbose_name=_('Project status'),
                              max_length=20)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))

    def __str__(self):
        return self.name

    def done_issues_in_project(self):
        count = 0
        for issue in self.issues.all():
            if issue.status == 'done':
                count += 1
        return count


class Issue(models.Model):

    ISSUE_TYPE_CHOICES = [
        ('task', 'Task'),
        ('bug', 'Bug')
    ]

    ISSUE_STATUS_CHOICES = [
        ('to do', 'To do'),
        ('in progress', 'In progress'),
        ('done', 'done'),
        ('cancel', 'cancel')
    ]

    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ]

    ENVIRONMENT_CHOICES = [
        ('local', 'Local'),
        ('dev', 'Development'),
        ('test', 'Test'),
        ('stage', 'Stage'),
        ('prod', 'Production')
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues', verbose_name=_('Project'))
    type = models.CharField(choices=ISSUE_TYPE_CHOICES, default='task', verbose_name=_('Issue type'),
                                  max_length=5)
    status = models.CharField(choices=ISSUE_STATUS_CHOICES, default='to do', verbose_name=_('Issue status'),
                                    max_length=20)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='low', verbose_name=_('Issue priority'),
                                max_length=10)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issues_assignee',
                                 verbose_name=_('Assignee'))
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issues_reporter',
                                 verbose_name=_('Reporter'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    summary = models.TextField(verbose_name=_('Summary'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
    environment = models.CharField(choices=ENVIRONMENT_CHOICES, default='local', verbose_name=_('Environment'),
                                max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def create_slug(self):
        project_slug = str(self.project.slug).upper()
        count_issue_in_project = Issue.objects.filter(project=self.project).count()
        if self.slug:
            issue_slug = self.slug
        else:
            issue_slug = f'{project_slug}-{count_issue_in_project+1}'
        return issue_slug

    def save(self, *args, **kwargs):
        self.slug = self.create_slug()
        return super().save()


    def __str__(self):
        return f'{self.summary} (project: {self.project})'


    def get_absolute_url(self):
        return reverse('issues:issue-detail', kwargs={'slug':self.slug})


class Comment(models.Model):
    text = models.TextField(verbose_name=_('Comment'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Author'))
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Issue'))

    def __str__(self):
        return f'Comment from issue {self.issue.summary}'


def get_attachment_path(instance, filename):
    datetime = pendulum.now('Europe/Warsaw')
    datetime = datetime.to_datetime_string().replace(':', '_')
    return 'uploads/{0}/{1}-{2}'.format(instance.issue.id, datetime, filename)


class Attachment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='attachments', verbose_name=_('Issue'))
    file = models.FileField(upload_to=get_attachment_path, verbose_name=_('File'))
    added = models.DateTimeField(auto_now_add=True, verbose_name=_('Added'))

    def __str__(self):
        return f'Attachment from issue {self.issue.summary} (id: {self.issue.id})'
