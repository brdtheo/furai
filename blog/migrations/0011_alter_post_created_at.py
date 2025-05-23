# Generated by Django 5.2 on 2025-05-13 18:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(db_comment='The creation date of the post', default=django.utils.timezone.now, help_text='The creation date of the post'),
        ),
    ]
