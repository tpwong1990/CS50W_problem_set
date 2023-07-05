from django.contrib import admin
from .models import User, List, Bid, Watch, closed_auction, list_comment, Category

# Register your models here.
admin.site.register(User)
admin.site.register(List)
admin.site.register(Bid)
admin.site.register(Watch)
admin.site.register(closed_auction)
admin.site.register(list_comment)
admin.site.register(Category)