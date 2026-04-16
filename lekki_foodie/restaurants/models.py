# Here We Create the models needed for the project.

from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)  # e.g., 4.5 out of 5

    def __str__(self):
        return self.name