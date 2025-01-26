from django.shortcuts import render , redirect
from django.views.generic import CreateView , View 
from .models import MemberModel
from .forms import SignupForm , LoginForm
from django.contrib import messages
from django.contrib.auth import login , authenticate 
from django.http import HttpResponse

# Create your views here.

class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'members/signup.html'
    success_url = 'login'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print("======= form is validated ============")
            form.save()
            messages.info(request, 'User Created Successfully')
            return redirect(self.success_url)
        else:
            print("======= form is not validated ============")
            context = {'form': form}
            return render(request, self.template_name, context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        member = authenticate(request , username = username , password = password)
        if member:
            login(request , member)
            return redirect('home')
        else:
            return render(request , 'members/login.html' , {'error' : 'invalid username or password'})
    return render(request , 'members/login.html')