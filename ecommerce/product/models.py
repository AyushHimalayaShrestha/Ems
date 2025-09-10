from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#  Model for Category
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category_name
    
# Model for Product
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    product_description=models.TextField()
    quantity=models.IntegerField()
    product_image=models.ImageField(upload_to='products/', null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE) 
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name 
    
# Cart
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Order
class Order(models.Model):
    PAYMENT_METHOD = (
        ("Cash On Delivery","Cash On Delivery"),
        ("Esewa","Esewa")
        
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    totalPrice = models.IntegerField()
    payment_method =models.CharField(choices=PAYMENT_METHOD)
    payment_status = models.CharField(default="Pending")
    email = models.EmailField()
    contact_no = models.CharField()
    address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# order item
class OrderItem(models.Model):
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)