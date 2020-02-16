from django.contrib import admin
from .models import Project, Issue, Comment, Attachment

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "slug", "created")
    search_fields = ("name",)
    list_filter = ("name", "status")
    ordering = ("created",)


class IssueAdmin(admin.ModelAdmin):
    list_display = ("summary", "project", "type", "priority", "assignee", "reporter")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "project",
                    "type",
                    "status",
                    "priority",
                    "assignee",
                    "reporter",
                    "summary",
                    "description",
                    "environment",
                )
            },
        ),
    )
    search_fields = ("summary", "project")
    list_filter = ("project", "type", "assignee", "reporter")
    ordering = ("project", "created")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("issue", "author", "created")
    search_fields = ("author", "issue")
    list_filter = ("issue", "author")
    ordering = ("created",)


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("issue", "file", "added")
    list_filter = ("issue",)
    ordering = ("added",)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Attachment, AttachmentAdmin)
