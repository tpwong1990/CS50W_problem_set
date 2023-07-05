from .models import User, List, Bid, Watch, closed_auction
from django.core.exceptions import ObjectDoesNotExist



def AddBid(user_id, item_id, price):
    model=Bid()
    model.buyer = User.objects.get(id=user_id)
    model.item = List.objects.get(id=item_id)
    model.bid_price = price
    model.save()

def CheckWatch(user_id, item_id):
    try:
        Watch.objects.get(item=item_id, watch_user=user_id)
    except ObjectDoesNotExist:
        return False
    else:
        return True
    
def AddWatch(user_id, item_id):
    add = Watch()
    add.item = List.objects.get(id=item_id)
    add.watch_user = User.objects.get(id=user_id)
    add.save()

def RemoveWatch(user_id, item_id):
    remove= Watch.objects.get(item=item_id, watch_user=user_id)
    remove.delete()

def FindHighestBidder(item_id):
    item = Bid.objects.filter(item=item_id)
    max = 0
    for price in item: 
        if price.bid_price > max:
            max = price.bid_price
    winner = Bid.objects.get(item=item_id, bid_price = max)
    winner = winner.buyer.username
    return winner

def CheckClose(item_id):
    try:
        closed_auction.objects.get(item=item_id)
    except ObjectDoesNotExist:
        return False
    else:
        return True