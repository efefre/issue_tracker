from django.urls import path

from .views import DashboardView, ProjectsListView, AddProjectView, EditProjectView, DeleteProjectView, \
    ProjectDetailView, IssueDetailView, AddIssueView, EditIssueView, DeleteAttachmentView, AddCommentView, \
    EditCommentView, DeleteCommentView, AssignedToMeView

app_name = 'issues'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('my-issues/', AssignedToMeView.as_view(), name='my-issues'),

    path('projects/', ProjectsListView.as_view(), name='projects-list'),
    path('projects/add/', AddProjectView.as_view(), name="add-project"),
    path('projects/<int:pk>/update/', EditProjectView.as_view(), name='update-project'),
    path('projects/<int:pk>/delete/', DeleteProjectView.as_view(), name='delete-project'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),


    path('projects/<slug:slug>/add/', AddIssueView.as_view(), name='add-issue'),
    path('projects/<str:slug>/<int:issue_slug>/', IssueDetailView.as_view(), name='issue-detail'),
    path('projects/<str:project_slug>/<slug:slug>/edit/', EditIssueView.as_view(), name='edit-issue'),

    path('projects/<str:project_slug>/<str:issue_slug>/<int:pk>/delete-attachment/', DeleteAttachmentView.as_view(), name='delete-attachment'),

    path('projects/<str:project_slug>/<slug:slug>/add-comment/', AddCommentView.as_view(), name='add-comment'),
    path('projects/<str:project_slug>/<str:issue_slug>/<int:pk>/edit-comment/', EditCommentView.as_view(), name='edit-comment'),
    path('projects/<str:project_slug>/<str:issue_slug>/<int:pk>/delete-comment/', DeleteCommentView.as_view(), name='delete-comment')
]
