from django import forms
from .models import MemberModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = MemberModel
        exclude = ['isActive']
        widgets ={
            'password': forms.PasswordInput(),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not username.isalnum() and not '_' in username:
            raise forms.ValidationError('username should only contain alphabetic characters or underscore!')
        if username[0].isdigit():
            raise forms.ValidationError('username can not start with a digit')
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')

        try:
            validate_password(password)
        except forms.ValidationError as e:
            self.add_error('password' , e.messages)
        return password
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if not first_name.isalnum():
            raise forms.ValidationError('first name should only contain alphabetic characters')
        
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('first_name')
        
        if not last_name.isalnum():
            raise forms.ValidationError('last name should only contain alphabetic characters')
        
        return last_name
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('the passwords does not match')
        if len(password) < 8 :
            raise forms.ValidationError('password should be atleast 8 characters long')
        return cleaned_data

        
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length= 200)
    password = forms.CharField(widget=forms.PasswordInput())
    