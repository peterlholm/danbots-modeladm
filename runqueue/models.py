"runques models"
from django.db import models

# Create your models here.

HOSTS = (('sal5','sal5'),('sal4','sal4'))

class RunQueue(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True )
    date = models.DateTimeField('date created', blank=True, null=True)
    hostname = models.CharField(max_length=40, choices=HOSTS)
    command = models.CharField(max_length=200,blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
