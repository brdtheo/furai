# Generated by Django 5.2 on 2025-05-13 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(db_comment='The creation date of the post', default=datetime.datetime(2025, 5, 13, 17, 58, 2, 756279, tzinfo=datetime.timezone.utc), help_text='The creation date of the post'),
        ),
    ]
