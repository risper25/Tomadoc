# Generated by Django 3.0.6 on 2020-10-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0019_prediction_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
