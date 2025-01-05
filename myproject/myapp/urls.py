from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('panel_admina', views.panel_admina, name='panel_admina'),
    path('panel_usera', views.panel_usera, name='panel_usera'),

    path('api/tickets/', views.TicketListView.as_view(), name='ticket-list'),  # Lista zgłoszeń
    path('api/upload/', views.FileUploadView.as_view(), name='file-upload'),  # Przesyłanie plików

    path('ws/chat/<int:ticket_id>/', views.chat_view, name='chat-view'),  
]
