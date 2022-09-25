from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter

from bidding.biddingmiddleware import TokenAuthMiddleware
from bidding.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddleware(
        URLRouter(websocket_urlpatterns)
    )
})
