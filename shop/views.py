from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Category   , OrderDetail
from .forms import OrderForm


# Create your views here.
def index(request, category_id=None):
    categories = Category.objects.all()
    search_query = request.GET.get('search')
    
    products = Product.objects.all()  # Avval barcha mahsulotlar olinadi

    if category_id:
        products = products.filter(category_id=category_id)  # oldingi product list ustidan filtrlanadi

    if search_query:
        products = products.filter(name__icontains=search_query)  # yana ustidan search bo‘yicha filtrlanadi

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'shop/detail.html', {'product': product})
    except Product.DoesNotExist:
        return render(request, '')

def order_detail(request,pk):
    product = get_object_or_404(Product,pk=pk)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('index')
    context = {
        'form':form,
        'product':product
    }
            
    return render(request,'shop/detail.html',context = context)
       