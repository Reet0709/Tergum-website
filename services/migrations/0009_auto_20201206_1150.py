# Generated by Django 3.0.8 on 2020-12-06 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_attachment_owner'),
        ('services', '0008_auto_20201206_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='instruction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.JobType'),
        ),
        migrations.AlterField(
            model_name='job',
            name='quality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Quality'),
        ),
        migrations.AlterField(
            model_name='job',
            name='source_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_language', to='common.Language'),
        ),
    ]
