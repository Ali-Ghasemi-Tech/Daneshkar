# Generated by Django 5.1.5 on 2025-02-01 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0007_rename_users_workspace_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='Workspace',
            new_name='workspace',
        ),
    ]
