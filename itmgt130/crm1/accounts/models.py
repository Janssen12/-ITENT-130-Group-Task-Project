from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=1000, null=True)
    profile_pic = models.ImageField(default="profile.png",null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 
    
class Product(models.Model):
    CATEGORY = (
        ('Sushi Rolls', 'Sushi Rolls'),
        ('Sashimi', 'Sashimi'),
        ('Onigiri', 'Onigiri'),
        
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag) 
    
    def __str__(self):
        return self.name or ""
 

    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    BRANCH = (
        ('Ortigas Avenue', 'Ortigas Avenue'),
        ('Shangri-La Plaza', 'Shangri-La Plaza'),
        ('Katipunan Avenue', 'Katipunan Avenue'),
    )
    
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200,null=True, blank=True, choices=STATUS)
    branch = models.CharField(max_length=200,null=True, blank=True, choices=BRANCH)
    note = models.CharField(max_length=1000, null=True)
    def __str__(self):
        return self.product.name if self.product else ""
       