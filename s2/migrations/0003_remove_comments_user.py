# Generated by Django 3.1.7 on 2021-06-10 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2', '0002_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='User',
        ),
    ]
