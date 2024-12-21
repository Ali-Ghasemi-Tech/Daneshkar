from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from .models import CustomeUserModel
class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomeUserModel
        fields = UserCreationForm.Meta.fields + ('bio' , 'picture')

class CustomeUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomeUserModel
        fields = UserChangeForm.Meta.fields