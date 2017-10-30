from django.db import models
# from payment.models import Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

# @login_required
# def add_to_cart(request,item_name):
#     item = get_object_or_404(Item, pk=item_name)
#     cart,created = Cart.objects.get_or_create(user=request.user, active=True)
#     order,created = Cart.objects.get_or_create(item=item,cart=cart)
#     order.quantity += 1
#     order.save()
#     messages.success(request, "Cart updated!")
#     return redirect('cart')

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length = 40)
    category = models.CharField(max_length = 40)
    sub_category = models.CharField(max_length = 40)
    item_logo = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits=10, decimal_places=3, default='0')

    def __str__(self):
        return self.item_name