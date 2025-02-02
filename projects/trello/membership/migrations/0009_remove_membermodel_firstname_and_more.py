# Generated by Django 5.1.5 on 2025-02-01 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_alter_membermodel_options_alter_membermodel_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membermodel',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='membermodel',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='membermodel',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='membermodel',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='membermodel',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
