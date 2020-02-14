from django import forms
from .models import Project, Issue, Attachment
from django.forms.models import inlineformset_factory


class AddProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'slug', 'status')

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Enter project name'}),
                   'slug': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Enter slug (only letters)'}),
                   'status': forms.Select(attrs={'class': 'form-control'})
                   }


class UpdateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'slug', 'status')

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Enter project name'}),
                   'slug': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Enter slug (only letters)'}),
                   'status': forms.Select(attrs={'class': 'form-control'})
                   }


class AddIssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('summary', 'status', 'type', 'priority', 'assignee', 'description', 'environment')

        widgets = {'summary': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Enter summary'}),
                   'description': forms.Textarea(attrs={'class': 'form-control',
                                                  'placeholder': 'Description'}),
                   'status': forms.Select(attrs={'class': 'form-control'}),
                   'type': forms.Select(attrs={'class': 'form-control'}),
                   'priority': forms.Select(attrs={'class': 'form-control'}),
                   'assignee': forms.Select(attrs={'class': 'form-control'}),
                   'environment': forms.Select(attrs={'class': 'form-control'})
                   }


class EditIssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('summary', 'status', 'type', 'priority', 'assignee', 'description', 'environment')

        widgets = {'summary': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Enter summary'}),
                   'description': forms.Textarea(attrs={'class': 'form-control',
                                                  'placeholder': 'Description'}),
                   'status': forms.Select(attrs={'class': 'form-control'}),
                   'type': forms.Select(attrs={'class': 'form-control'}),
                   'priority': forms.Select(attrs={'class': 'form-control'}),
                   'assignee': forms.Select(attrs={'class': 'form-control'}),
                   'environment': forms.Select(attrs={'class': 'form-control'})
                   }


class AddAttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        exclude = ()


AttachmentFormset = inlineformset_factory(Issue, Attachment,
                                          form = AddAttachmentForm,
                                          fields= ['file',], extra=1, can_delete=True)
