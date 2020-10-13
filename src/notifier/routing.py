from channels.routing import URLRouter
from django.urls import path

from .consumers import EchoConsumer

websocket_urlpatterns = [
    path('ws/', URLRouter([
        path('', EchoConsumer),
    ])),
]
