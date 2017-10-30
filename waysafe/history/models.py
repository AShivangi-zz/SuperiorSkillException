from django.db import models
#from homepage.models import customer
#from aisle.models import item


# Create your models here.
class history(models.Model):
    last_order = models.CharField(max_length=40, default='NULL')
    #user_name = models.ForeignKey(customer, on_delete=models.CASCADE, default='NULL')
    #last_order = models.ForeignKey(order, on_delete=models.CASCADE, default='NULL')
    # previous orders

   # def __str__(self):
      #  return self.user_name + " " + self.last_order


class order(models.Model):
    order_name = models.CharField(max_length=40, default='NULL')
    #user_name = models.ForeignKey(customer, on_delete=models.CASCADE, default='NULL')
    #itemName = models.ForeignKey(item.item_name, on_delete=models.CASCADE, default='NULL')
    #price = models.ForeignKey(item.price, on_delete=models.CASCADE, default='NULL')