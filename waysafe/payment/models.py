from django.db import models
from homepage.models import customer
from aisle.models import Item

class Cart(models.Model):
    user = models.ForeignKey(customer)
    item = models.ForeignKey(Item)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)

    def __unicode__(self):
            return "%s" % (self.user)

 #Create your models here.
class payment(models.Model):
    user_name = models.ForeignKey(customer, on_delete=models.CASCADE, default='NULL')
    card_number = models.FloatField(default='NULL')
    CVV = models.FloatField(default='NULL')
    expiry_month=models.FloatField(default='NULL')
    expiry_year=models.FloatField(default='NULL')


    def __str__(self):
        return self.card_number

