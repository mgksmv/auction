from django.conf import settings
from rest_framework.serializers import ModelSerializer
from rest_framework.relations import StringRelatedField
from rest_framework.fields import DateTimeField

from .models import Item, Auction, Bid
from accounts.serializers import UserSerializer


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class BidSerializer(ModelSerializer):
    auction = StringRelatedField(read_only=True)
    user = UserSerializer(read_only=True)
    bid_placed_at = DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = Bid
        fields = '__all__'


class AuctionSerializer(ModelSerializer):
    item = ItemSerializer(read_only=True)
    bids = BidSerializer(many=True, read_only=True)
    winner = UserSerializer(read_only=True)

    class Meta:
        model = Auction
        fields = '__all__'
