from django.db import models

# Create your models here.

class Sample(models.Model):
    sample = models.TextField(max_length=120)
