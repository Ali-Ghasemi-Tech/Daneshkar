from django.contrib import admin
from .models import Workspace , Board , Task

# Register your models here.

class WorkspaceAdmin(admin.ModelAdmin):
    filter_horizontal = ['members']
    
admin.site.register(Workspace , WorkspaceAdmin)

class BoardAdmin(admin.ModelAdmin):
    filter_horizontal = ['users']

admin.site.register(Board , BoardAdmin)


admin.site.register(Task)

