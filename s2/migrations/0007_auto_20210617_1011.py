# Generated by Django 3.1.7 on 2021-06-17 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2', '0006_auto_20210616_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enq',
            old_name='email',
            new_name='emailenq',
        ),
    ]