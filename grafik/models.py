# models.py
from django.db import models

class ChartData(models.Model):
    month = models.CharField(max_length=20)
    actual_value = models.FloatField()
    target_value = models.FloatField()
