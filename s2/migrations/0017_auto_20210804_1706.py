# Generated by Django 3.1.7 on 2021-08-05 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2', '0016_post_cate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='category',
            field=models.CharField(default='books', max_length=100),
        ),
    ]
