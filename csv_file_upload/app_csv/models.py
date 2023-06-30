from django.db import models

# Create your models here.
class Employee(models.Model):
    year_experience = models.FloatField()
    salary = models.FloatField()