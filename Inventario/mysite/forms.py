from django import forms
from .models import product

class productform(forms.ModelForm):
    class Meta:
        model = product
        fields = ("product_code", "name" , "quantity")