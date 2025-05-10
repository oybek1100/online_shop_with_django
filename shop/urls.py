from django.urls import path
from .views import index  # Import the index view from views.py
from .views import product_detail , OrderDetail # Import the details view from views.py
from . import views 

urlpatterns = [
    path('', index, name='index'), 
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'), 
    path('category/<int:category_id>/', views.index, name='category_products'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
]
