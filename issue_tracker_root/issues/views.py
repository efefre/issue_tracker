from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, FormView, UpdateView

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
