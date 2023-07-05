from django.contrib import admin
from .models import Item, Category, ProductImage, User, ShoppingCart, PlacedOrder, OrderStatus

# Register your models here.
admin.site.register(User)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ShoppingCart)
admin.site.register(PlacedOrder)
admin.site.register(OrderStatus)