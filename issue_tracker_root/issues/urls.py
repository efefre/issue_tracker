from django.urls import path

from .views import DashboardView, ProjectsListView

app_name = 'issues'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('projects/', ProjectsListView.as_view(), name='projects-list'),
]