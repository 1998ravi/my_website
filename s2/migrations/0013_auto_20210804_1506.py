# Generated by Django 3.1.7 on 2021-08-05 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2', '0012_auto_20210804_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(default='from website', max_length=100),
        ),
    ]
