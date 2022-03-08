# Generated by Django 4.0.1 on 2022-03-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_trainingmodel_input_file_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimulationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='date created')),
                ('data', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]