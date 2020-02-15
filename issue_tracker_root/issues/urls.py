from django.urls import path

from .views import DashboardView, ProjectsListView, AddProjectView, EditProjectView, DeleteProjectView, \
    ProjectDetailView, IssueDetailView, AddIssueView, EditIssueView, DeleteAttachmentView, AddCommentView, \
    EditCommentView, DeleteCommentView, AssignedToMeView

app_name = 'issues'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('my-issues/', AssignedToMeView.as_view(), name='my-issues'),

    path('projects/', ProjectsListView.as_view(), name='projects-list'),
    path('projects/add', AddProjectView.as_view(), name="add-project"),
    path('projects/<int:pk>/update', EditProjectView.as_view(), name='update-project'),
    path('projects/<int:pk>/delete', DeleteProjectView.as_view(), name='delete-project'),
    path('projects/<slug:slug>', ProjectDetailView.as_view(), name='project-detail'),

    path('<slug:slug>/', IssueDetailView.as_view(), name='issue-detail'),
    path('project/<slug:slug>/add', AddIssueView.as_view(), name='add-issue'),
    path('<slug:slug>/edit', EditIssueView.as_view(), name='edit-issue'),

    path('delete-attachment/<int:pk>/', DeleteAttachmentView.as_view(), name='delete-attachment'),

    path('<slug:slug>/add-comment', AddCommentView.as_view(), name='add-comment'),
    path('edit-comment/<int:pk>', EditCommentView.as_view(), name='edit-comment'),
    path('delete-comment/<int:pk>', DeleteCommentView.as_view(), name='delete-comment')
]
