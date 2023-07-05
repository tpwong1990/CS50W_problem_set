from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / item_<id>/<filename>
    return 'images/item_{0}/{1}'.format(instance.id, filename)

def user_directory_path_product_image(instance, filename):
    # file will be uploaded to MEDIA_ROOT / item_<id>/<filename>
    return 'images/item_{0}/{1}'.format(instance.product.id, filename)

# Create your models here.

class User(AbstractUser):
    # first_name =  models.CharField(max_length=50)
    # last_name =  models.CharField(max_length=50)
    phone_no = PhoneNumberField(null=True, blank=True, unique=True)

class Category(models.Model):
    list = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    updated_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    cover_image = models.ImageField(blank=True, upload_to = user_directory_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=True)
    stock = models.IntegerField()
    code = models.CharField(max_length=20, unique=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(blank=True, upload_to = user_directory_path_product_image)

class ShoppingCart(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class OrderStatus(models.Model):
    status = models.CharField(max_length=100)

class PlacedOrder(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="have_order")
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now_add=True)
