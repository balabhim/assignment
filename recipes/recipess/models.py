from django.db import models

class Recipes(models.Model):
    name = models.CharField(max_length=50)
    discriptions=models.CharField(max_length=500)

    def __str__(self):
        return self.name
