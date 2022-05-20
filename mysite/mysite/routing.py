from channels.auth import AuthMiddlewareStack 
from  channels.routing import ProtocolTypeRouter,URLRouter
import hanash.routing
application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            hanash.routing.websocket_urlpatterns
        )
    ),
})