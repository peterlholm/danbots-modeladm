# Generated by Django 4.0.2 on 2022-03-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_simulationmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulationmodel',
            name='data',
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='analytic_path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='background',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='batch_trainin_path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='file_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='light_intensity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='lights_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='material',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='sample_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='sim_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='simulation_path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='single_training_path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
