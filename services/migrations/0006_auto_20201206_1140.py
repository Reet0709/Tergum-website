# Generated by Django 3.0.8 on 2020-12-06 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20201206_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateField(null=True, verbose_name='deadline for delivery'),
        ),
        migrations.AlterField(
            model_name='job',
            name='word_count',
            field=models.IntegerField(null=True),
        ),
    ]
