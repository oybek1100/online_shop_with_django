from django.shortcuts import render
from .models import Product, Category


# Create your views here.
def index(request):
    
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'shop/home.html' , context)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'shop/detail.html', {'product': product})
    except Product.DoesNotExist:
        return render(request, '')