# Generated by Django 5.1.4 on 2025-01-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_post_dislike_alter_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post_pics/'),
        ),
    ]
