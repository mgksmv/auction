from rest_framework.routers import DefaultRouter

from .views import ItemViewSet, AuctionViewSet, BidViewSet

router = DefaultRouter()

router.register(r'items', ItemViewSet)
router.register(r'auctions', AuctionViewSet)
router.register(r'bids', BidViewSet)

app_name = 'bidding'

urlpatterns = router.urls
