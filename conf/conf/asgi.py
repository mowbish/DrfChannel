import os
import currencies.routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from currencies.consumers import WSConsumer
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")


application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": get_asgi_application(),
    # WebSocket chat handler
    "websocket":
        AuthMiddlewareStack(
        URLRouter([
            # currencies.routing.websocket_urlpatterns
            re_path("ws/some_url", WSConsumer.as_asgi()),]))
})
