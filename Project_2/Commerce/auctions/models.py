from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return str(self.id) 

class Category(models.Model):
    name = models.CharField(max_length=100)


class List(models.Model):
    item_name = models.CharField(max_length=100)
    floor_price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=1000)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Listed_item")
    image = models.CharField(max_length=1000, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = "list_of_this_category")
    no_bid = models.IntegerField(default = 0)
    current_price = models.DecimalField(max_digits=20, decimal_places=2, default=floor_price)

class Bid(models.Model):
    buyer = models.ForeignKey(User,on_delete=models.CASCADE, related_name="placed_bid")
    item = models.ForeignKey(List, on_delete=models.CASCADE, related_name="bid_detail")
    bid_price = models.DecimalField(max_digits=20, decimal_places=2)
 

class Watch(models.Model):
    item = models.ForeignKey(List, on_delete=models.CASCADE, related_name="watched_detail")
    watch_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")

class closed_auction(models.Model):
    item = models.ForeignKey(List, on_delete=models.CASCADE, related_name="closed_list")
    winner = models.ForeignKey(User, on_delete=models.CASCADE)

class list_comment(models.Model):
    item = models.ForeignKey(List, on_delete=models.CASCADE, related_name="item_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    comment = models.CharField(max_length=1000)
