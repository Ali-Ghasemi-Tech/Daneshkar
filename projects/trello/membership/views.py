from django.shortcuts import render , redirect
from django.views.generic import CreateView , View 
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login , authenticate 


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView

from .API.serializers import SignupSerializer

# Create your views here.

class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'members/signup.html'
    success_url = 'login'
   
    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         print("======= form is validated ============")
    #         form.save()
    #         messages.info(request, 'User Created Successfully')
    #         return redirect(self.success_url)
    #     else:
    #         print("======= form is not validated ============")
    #         context = {'form': form}
    #         return render(request, self.template_name, context)

# def loginView(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         member = authenticate(request , username = username , password = password)
#         if member:
#             login(request , member)
#             return redirect('home')
#         else:
#             return render(request , 'members/login.html' , {'error' : 'invalid username or password'})
#     return render(request , 'members/login.html')