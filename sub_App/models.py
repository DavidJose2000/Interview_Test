from django.db import models

# Create your models here.


class Expense:
    name = models.CharField(30)
    amount = models.FloatField()
    category = models.CharField(30)
    
    def __str__(self):
        return f"{self.name}- {self.amount} - {self.category}"