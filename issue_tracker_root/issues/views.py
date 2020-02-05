from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, FormView, UpdateView, DeleteView

from .forms import AddProjectForm, UpdateProjectForm
from .models import Issue, Project


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    model = Issue
    template_name = 'issues/dashboard.html'


@method_decorator(login_required, name='dispatch')
class ProjectsListView(ListView):
    model = Project
    template_name = 'issues/projects_list.html'

    def get_queryset(self):
        query = super().get_queryset().order_by('-created')
        return query


@method_decorator(login_required, name='dispatch')
class AddProjectView(FormView):
    template_name = 'issues/add_project.html'
    form_class = AddProjectForm
    success_url = '/projects'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UpdateProjectView(UpdateView):
    model = Project
    template_name = 'issues/update_project.html'
    form_class = UpdateProjectForm

    def get_success_url(self):
        return reverse('issues:projects-list')


@method_decorator(login_required, name='dispatch')
class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'issues/confirm_delete_project.html'
    context_object_name = 'delete_project'
    success_url = '/projects'


@method_decorator(login_required, name='dispatch')
class ProjectDetailView(ListView):
    model = Issue
    template_name = 'issues/project_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['issues_in_project'] = Issue.objects.filter(project__slug=slug).order_by('-created')
        context['tasks_in_project'] = Issue.objects.filter(project__slug=slug, type='task').order_by('-created')
        context['bugs_in_project'] = Issue.objects.filter(project__slug=slug, type='bug').order_by('-created')
        context['project_detail'] = Project.objects.get(slug=slug)
        return context
