# Generated by Django 3.0.6 on 2020-10-29 12:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diagnose', '0025_auto_20201029_1210'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_profile',
            new_name='Profile',
        ),
    ]
