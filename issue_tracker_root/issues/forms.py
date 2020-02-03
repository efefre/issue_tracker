from django import forms
from .models import Project


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
