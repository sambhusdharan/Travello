from django.db import models

# Create your models here.
class searching (models.Model):
    city_search=models.CharField(max_length=100)
    departure_search=models.TextField()
    arrival_search=models.TextField()
    budget_search=models.IntegerField()
