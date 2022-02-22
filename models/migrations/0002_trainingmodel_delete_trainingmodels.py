# Generated by Django 4.0.1 on 2022-01-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date created')),
                ('hostname', models.CharField(max_length=40)),
                ('history_path', models.CharField(max_length=200)),
                ('model_path', models.CharField(max_length=200)),
                ('figures_dir', models.CharField(max_length=200)),
                ('dict_text_output_path', models.CharField(max_length=200)),
                ('checkpoint_path', models.CharField(max_length=200)),
                ('test_indexes_list_path', models.CharField(max_length=200)),
                ('imagecount', models.IntegerField()),
                ('num_training_img', models.IntegerField()),
                ('num_validation_img', models.IntegerField()),
                ('epocs', models.IntegerField()),
                ('batch_size', models.IntegerField()),
                ('loss', models.CharField(max_length=20)),
                ('metrics', models.CharField(max_length=20)),
                ('optimizer', models.CharField(max_length=20)),
                ('power', models.IntegerField()),
                ('n_blocks', models.IntegerField()),
                ('normalization', models.CharField(max_length=20)),
                ('learning_rate', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='TrainingModels',
        ),
    ]