# Generated by Django 5.1.4 on 2025-01-10 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_commentmodel_level_alter_post_time_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='level',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_post',
            field=models.TimeField(default=datetime.datetime(2025, 1, 10, 21, 21, 27, 400831, tzinfo=datetime.timezone.utc)),
        ),
    ]
