# Generated by Django 5.1.4 on 2025-01-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_post_time_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_pics/')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
