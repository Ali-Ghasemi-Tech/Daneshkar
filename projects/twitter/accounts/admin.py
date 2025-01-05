from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomeUserChangeForm , CustomeUserCreationForm
from .models import CustomeUserModel

# Register your models here.

class CustomeUserAdmin(UserAdmin):
    add_form = CustomeUserCreationForm
    form = CustomeUserChangeForm
    model =CustomeUserModel
    list_display = ['username' , 'first_name' , 'last_name' , 'is_superuser' , 'date_joined']
    filter_horizontal = ['follow']
    fieldsets = UserAdmin.fieldsets + (
        ('personalizations' , {"fields" : ('bio', 'picture')}) , 
        ('follows' , {"fields": ('follow' ,)})
    )

admin.site.register(CustomeUserModel ,CustomeUserAdmin)