from django import forms
from .models import Product, OrderDetail

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        exclude = ['created_at', 'updated_at' , 'product']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


