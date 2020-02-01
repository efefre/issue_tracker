from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .models import Issue


@method_decorator(login_required, name='dispatch')
class DashboardView(ListView):
    model = Issue
    template_name = 'issues/dashboard.html'

