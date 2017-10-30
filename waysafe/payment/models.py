from django.db import models
from homepage.models import customer

 #Create your models here.
class payment(models.Model):
    user_name = models.ForeignKey(customer, on_delete=models.CASCADE, default='NULL')
    card_number = models.FloatField(default='NULL')
    CVV = models.FloatField(default='NULL')
    expiry_month=models.FloatField(default='NULL')
    expiry_year=models.FloatField(default='NULL')


    def __str__(self):
        return self.card_number