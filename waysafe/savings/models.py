from django.db import models
from homepage.models import customer

# Create your models here.
class cupon(models.Model):
    cupon_name = models.CharField(max_length = 40)
    discount = models.IntegerField()

    def __str__(self):
        return self.cupon_name