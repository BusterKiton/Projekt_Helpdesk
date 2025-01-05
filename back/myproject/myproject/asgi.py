"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import Projekt_Helpdesk.back.myproject.myapp.routing  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Django ASGI application
django_asgi_app = get_asgi_application()

# ProtocolTypeRouter konfiguracja
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Obsługa HTTP przez Django
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Projekt_Helpdesk.back.myproject.myapp.routing.websocket_urlpatterns  # Routing WebSocket
        )
    ),
})

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()
