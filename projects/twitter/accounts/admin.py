from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomeUserChangeForm , CustomeUserCreationForm
from .models import CustomeUserModel

# Register your models here.

class CustomeUserAdmin(UserAdmin):
    add_form = CustomeUserCreationForm
    form = CustomeUserChangeForm
    model =CustomeUserModel
    fieldsets = UserAdmin.fieldsets + (
        ('personalizations' , {"fields" : ('bio', 'picture')}) , 
    )

admin.site.register(CustomeUserModel ,CustomeUserAdmin)