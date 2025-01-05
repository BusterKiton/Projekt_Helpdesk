from django.urls import path
from ....myproject.myapp import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:ticket_id>/', consumers.ChatConsumer.as_asgi()),
]
