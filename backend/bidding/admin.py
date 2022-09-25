from django.contrib import admin

from .models import Category, Item, Wishlist, Auction, Bid

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Wishlist)
admin.site.register(Auction)
admin.site.register(Bid)
