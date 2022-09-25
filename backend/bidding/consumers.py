import json

from django.core.serializers import serialize
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Auction, Bid


class BidConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.auction_id = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = f'bid_{self.auction_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        commands = {
            'get_bids': self.get_bids,
            'place_new_bid': self.place_new_bid,
        }
        data = json.loads(text_data)
        received_command = data['command']
        if received_command in commands:
            await commands[received_command](data)

    @database_sync_to_async
    def get_bids(self, data):
        auction = Auction.objects.get(id=self.auction_id)
        bids = Bid.objects.filter(auction=auction)
        bids_json = serialize('json', bids)

        self.send(text_data=json.dumps({
            'command': 'get_bids',
            'messages': bids_json,
        }))

    async def place_new_bid(self, data):
        bid_message = data['bid']
        current_price = data['current_price']

        bid = await self.place_bid(float(bid_message), float(current_price))
        if bid:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'new_bid',  # new_bid function (handler)
                    'bid': bid,
                }
            )

    async def new_bid(self, event):
        bid = event['bid']

        await self.send(text_data=json.dumps({
            'command': 'get_bids',
            'bid': bid,
        }))

    @database_sync_to_async
    def place_bid(self, bid, current_price):
        if bid > current_price:
            user = self.scope['user']

            auction = Auction.objects.get(id=self.auction_id)
            auction.price = int(bid)
            auction.winner = user
            auction.save()

            winner = serialize('json', [user])

            bid_obj = Bid.objects.create(
                auction=auction,
                user=user,
                price=bid,
            )

            return {
                'user': user.get_full_name,
                'price': bid_obj.price,
                'winner': winner,
                'bid_placed_at': bid_obj.bid_placed_at.strftime(settings.DATETIME_FORMAT),
            }
