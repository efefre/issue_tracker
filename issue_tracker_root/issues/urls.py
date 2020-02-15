from django.urls import path

from .views import DashboardView, ProjectsListView, AddProjectView, UpdateProjectView, DeleteProjectView, \
    ProjectDetailView, IssueDetailView, AddIssueView, EditIssueView, DeleteAttachmentView, AddCommentView, \
    EditCommentView

app_name = 'issues'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('projects/', ProjectsListView.as_view(), name='projects-list'),
    path('add-project', AddProjectView.as_view(), name="add-project"),
    path('update-project/<int:pk>', UpdateProjectView.as_view(), name='update-project'),
    path('delete-project/<int:pk>', DeleteProjectView.as_view(), name='delete-project'),
    path('project/<slug:slug>', ProjectDetailView.as_view(), name='project-detail'),
    path('<slug:slug>/', IssueDetailView.as_view(), name='issue-detail'),
    path('project/<slug:slug>/add', AddIssueView.as_view(), name='add-issue'),
    path('<slug:slug>/edit', EditIssueView.as_view(), name='edit-issue'),
    path('delete-attachment/<int:pk>/', DeleteAttachmentView.as_view(), name='delete-attachment'),
    path('<slug:slug>/add-comment', AddCommentView.as_view(), name='add-comment'),
    path('edit-comment/<int:pk>', EditCommentView.as_view(), name='edit-comment')
]
