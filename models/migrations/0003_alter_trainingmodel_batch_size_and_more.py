# Generated by Django 4.0.2 on 2022-02-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_trainingmodel_delete_trainingmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingmodel',
            name='batch_size',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='checkpoint_path',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='dict_text_output_path',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='epocs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='figures_dir',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='history_path',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='hostname',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='imagecount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='learning_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='loss',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='metrics',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='model_path',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='n_blocks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='normalization',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='num_training_img',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='num_validation_img',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='optimizer',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='power',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainingmodel',
            name='test_indexes_list_path',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
