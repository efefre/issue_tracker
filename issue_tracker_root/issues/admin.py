from django.contrib import admin
from .models import Project, Issue, Comment, Attachment
# Register your models here.


class IssueAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('project', 'type', 'status', 'priority', 'assignee', 'reporter',
                       'summary', 'description', 'environment')
        }),
    )

admin.site.register(Project)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment)
admin.site.register(Attachment)