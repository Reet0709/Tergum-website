# Generated by Django 3.0.8 on 2020-12-06 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20201120_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_number',
            new_name='job_id',
        ),
    ]
