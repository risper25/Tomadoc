# Generated by Django 3.0.6 on 2020-11-19 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0037_auto_20201119_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='dis',
        ),
    ]
