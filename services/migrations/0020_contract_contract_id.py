# Generated by Django 3.0.8 on 2021-01-30 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_auto_20210129_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_id',
            field=models.CharField(default="1", max_length=25, unique=True),
            preserve_default=False,
        ),
    ]
