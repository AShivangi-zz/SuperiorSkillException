from django import forms
from django.contrib.auth.models import User
from .models import item

class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['item_name','catagory','sub_category','item_logo', 'price']