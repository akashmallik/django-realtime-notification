from channels.routing import ProtocolTypeRouter, URLRouter
import notifier.routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        notifier.routing.websocket_urlpatterns
    )
})
