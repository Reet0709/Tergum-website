# Generated by Django 3.0.8 on 2021-01-29 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0017_auto_20210129_2050'),
        ('services', '0017_job_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='dependency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.Contract'),
        ),
        migrations.AddField(
            model_name='contract',
            name='status',
            field=models.CharField(choices=[('TR', 'Translating'), ('PF', 'Proofreading')], default='TR', max_length=2),
        ),
        migrations.AddField(
            model_name='contract',
            name='target_language',
            field=models.ManyToManyField(related_name='contract_target_language', to='common.Language'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
