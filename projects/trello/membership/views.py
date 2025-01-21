from django.shortcuts import render
from django.views.generic import CreateView
from .models import MemberModel
from .forms import SignupForm
# Create your views here.

class SignUpView(CreateView):
    form_class = SignupForm
    model = MemberModel
    template_name = 'memebers/signup.html'
    success_url = 'admin'