# Generated by Django 3.1.7 on 2021-08-05 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2', '0015_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='s2.cat'),
        ),
    ]