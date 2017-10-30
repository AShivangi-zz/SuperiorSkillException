from django.db import models
from homepage.models import customer

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length = 40)
    category = models.CharField(max_length = 40)
    sub_category = models.CharField(max_length = 40)
    item_logo = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits=10, decimal_places=3, default='0')

    def __str__(self):
        return self.item_name