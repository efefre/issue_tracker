from django import forms
from django.core.exceptions import ValidationError

from .models import Project, Issue, Attachment, Comment
from django.forms.models import inlineformset_factory


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "slug", "status")

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter project name"}
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter slug (only letters)",
                }
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
        }


class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "slug", "status")

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter project name"}
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter slug (only letters)",
                }
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
        }


class AddIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = (
            "summary",
            "status",
            "type",
            "priority",
            "assignee",
            "description",
            "environment",
        )

        widgets = {
            "summary": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter summary"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Description"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "type": forms.Select(attrs={"class": "form-control"}),
            "priority": forms.Select(attrs={"class": "form-control"}),
            "assignee": forms.Select(attrs={"class": "form-control"}),
            "environment": forms.Select(attrs={"class": "form-control"}),
        }


class EditIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = (
            "summary",
            "status",
            "type",
            "priority",
            "assignee",
            "description",
            "environment",
        )

        widgets = {
            "summary": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter summary"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Description"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "type": forms.Select(attrs={"class": "form-control"}),
            "priority": forms.Select(attrs={"class": "form-control"}),
            "assignee": forms.Select(attrs={"class": "form-control"}),
            "environment": forms.Select(attrs={"class": "form-control"}),
        }


class AddAttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        exclude = ()

## Validation
    def clean_file(self):
        cleaned_data = super().clean()
        file = cleaned_data["file"]
        allowed_extensions = ["pdf", "jpg"]
        file_ext = str(file).split(".")[-1]

        if file_ext not in allowed_extensions:
            self.add_error("file", "File couldn't be uploaded. Wrong extension.")
            raise ValidationError("Wrong extension")
        else:
            return file


class AttachmentFormset(
    forms.inlineformset_factory(
        Issue,
        Attachment,
        form=AddAttachmentForm,
        fields=["file",],
        extra=1,
        can_delete=True,
    )
):
    def clean(self):
        error = False
        for form in self.forms:
            # print(form)
            if not form.is_valid():
                error = True

        if error:
            raise ValidationError("Wrong extension!")


# AttachmentFormset = inlineformset_factory(
#     Issue,
#     Attachment,
#     form=AddAttachmentForm,
#     fields=["file",],
#     extra=1,
#     can_delete=True,
# )


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)

        widgets = {
            "text": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Your comment..."}
            )
        }


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)

        widgets = {
            "text": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Your comment..."}
            )
        }
