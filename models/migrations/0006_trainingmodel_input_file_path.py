# Generated by Django 4.0.1 on 2022-03-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_remove_trainingmodel_epocs_trainingmodel_epochs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingmodel',
            name='input_file_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
