from rest_framework.viewsets import ModelViewSet

from .models import Item, Auction, Bid
from .serializers import ItemSerializer, AuctionSerializer, BidSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AuctionViewSet(ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer


class BidViewSet(ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
