# Generated by Django 3.0.6 on 2020-11-06 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0027_auto_20201030_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='description',
            field=models.CharField(max_length=50000),
        ),
    ]
