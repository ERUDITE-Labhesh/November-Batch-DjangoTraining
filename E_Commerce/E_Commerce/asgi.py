"""
ASGI config for E_Commerce project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'E_Commerce.settings')

from Channels_app import routing

# application = get_asgi_application()
application =ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        # Add more ASGI application URLs here
        "websocket": URLRouter(routing.ws_urlpatterns)
    }
)
