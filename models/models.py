"Models for Modeladmin"
from django.db import models

class TrainingModel(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True )
    date = models.DateTimeField('date created', blank=True, null=True)
    hostname = models.CharField(max_length=40, blank=True, null=True)
    history_path = models.CharField(max_length=200,blank=True, null=True)
    model_path = models.CharField(max_length=200, blank=True, null=True)
    input_file_path = models.CharField(max_length=200, blank=True, null=True)
    figures_dir = models.CharField(max_length=200, blank=True, null=True)
    dict_text_output_path = models.CharField(max_length=200, blank=True, null=True)
    checkpoint_path = models.CharField(max_length=200, blank=True, null=True)
    test_indexes_list_path = models.CharField(max_length=200, blank=True, null=True)
    test_indexes_list_path = models.CharField(max_length=200, blank=True, null=True)
    imagecount = models.IntegerField(blank=True, null=True)
    num_training_img = models.IntegerField(blank=True, null=True)
    num_validation_img = models.IntegerField(blank=True, null=True)
    epochs = models.IntegerField(blank=True, null=True)
    batch_size = models.IntegerField(blank=True, null=True)
    loss = models.CharField(max_length=20, blank=True, null=True)
    metrics = models.CharField(max_length=20, blank=True, null=True)
    optimizer = models.CharField(max_length=20, blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    n_blocks = models.IntegerField(blank=True, null=True)
    normalization = models.CharField(blank=True, max_length=20, null=True)
    learning_rate = models.FloatField(blank=True, null=True)
    training_data_path = models.CharField(blank=True, max_length=200, null=True)
    sim_seen_score = models.IntegerField(blank=True, null=True)
    sim_unseen_score = models.IntegerField(blank=True, null=True)
    wand_score = models.IntegerField(blank=True, null=True)
