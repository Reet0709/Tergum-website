# Generated by Django 3.0.8 on 2021-02-20 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0033_auto_20210220_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
