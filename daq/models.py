from django.db import models

# Create your models here.

class Tnh(models.Model):
    temperature = models.FloatField(default=None)
    humidity = models.FloatField(default=None)
    meas_date = models.DateTimeField('date measured')

