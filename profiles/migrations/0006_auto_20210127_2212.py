# Generated by Django 3.0.8 on 2021-01-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_delete_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(choices=[('TR', 'Translator'), ('ED', 'Editor'), ('MA', 'Manager'), ('SE', 'Secretary'), ('AC', 'Accountant'), ('IN', 'Interpreter'), ('OT', 'Other')], default='TR', max_length=2),
        ),
    ]
