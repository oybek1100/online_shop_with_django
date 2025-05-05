from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products' , null=True, blank=True)

    @property
    def discounted_price(self):
        if self.discount:
            return self.price - (self.price * self.discount / 100)
        return self.price
    
    