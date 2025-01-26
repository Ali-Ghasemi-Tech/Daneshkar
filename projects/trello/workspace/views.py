from django.shortcuts import render
from django.views.generic import ListView
from .models import Workspace

# Create your views here.

class HomePageView(ListView):
    model = Workspace
    template_name = 'home.html'
    