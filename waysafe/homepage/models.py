from django.db import models


"""
is a blueprint for your database.

It's how you are going to store data for your app. 
"""
# Create your models here.

class customer(models.Model):
    user_name = models.CharField(max_length = 40, default="NULL")
    street_address = models.CharField(max_length = 40)
    state = models.CharField(max_length=20)
    zipcode = models.FloatField()
    password = models.CharField(max_length = 20)
    phone_number = models.FloatField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user_name