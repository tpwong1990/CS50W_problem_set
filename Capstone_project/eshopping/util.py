from django.core.exceptions import ObjectDoesNotExist
from .models import ShoppingCart
    
no_item_per_page = 9

def check_exist_shopping_cart(user, item):
    try:
        exist_cart = ShoppingCart.objects.get(buyer=user, wished_item=item)
    except ObjectDoesNotExist:
        return False
    else:
        return True