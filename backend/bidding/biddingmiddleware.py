from urllib.parse import parse_qs

from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware


@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        token_key = scope['query_string'].decode('utf8').split('=')[1]

        if token_key:
            scope['user'] = await get_user(token_key)
            close_old_connections()
        else:
            scope['user'] = AnonymousUser()

        return await super().__call__(scope, receive, send)
