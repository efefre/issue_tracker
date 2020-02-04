from django.urls import path

from .views import DashboardView, ProjectsListView, AddProjectView, UpdateProjectView, DeleteProjectView, \
    ProjectDetailView

app_name = 'issues'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('projects/', ProjectsListView.as_view(), name='projects-list'),
    path('add-project', AddProjectView.as_view(), name="add-project"),
    path('update-project/<int:pk>', UpdateProjectView.as_view(), name='update-project'),
    path('delete-project/<int:pk>', DeleteProjectView.as_view(), name='delete-project'),
    path('project/<slug:slug>', ProjectDetailView.as_view(), name='project-detail'),
]