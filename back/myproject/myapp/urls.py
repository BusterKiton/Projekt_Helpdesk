from django.urls import path, include
from . import views
from .views import (HelloWorld, RegisterView, LoginAPIView
, UserTicketsApiView, WorkerTicketsApiView, TicketApiView, FreeTicketsApiView, TakeTicketsApiView)

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('panel_admina/', views.panel_admina, name='panel_admina'),
    path('panel_usera/', views.panel_usera, name='panel_usera'),

    path('api/hello/', HelloWorld.as_view(), name='hello-world'),
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/login/', LoginAPIView.as_view(), name='api-login'),
    path('api/tickets/', UserTicketsApiView.as_view(), name='user-tickets'),
    path('api/free_tickets/', FreeTicketsApiView.as_view(), name='user-tickets'),
    path('api/get_ticket/<int:id>/', TakeTicketsApiView.as_view(), name='user-tickets'),
    path('api/worker/tickets/', WorkerTicketsApiView.as_view(), name='worker-tickets'),
    path('api/ticket/<int:id>/', TicketApiView.as_view(), name='ticket'),
    # api/user              informacje o użytkowniku / edycja danych użytkownika
    # api/worker/ticket     ubsługa ticketu przez pracownika
    # api/ticket            wyświetlanie ticketu przez użytkownika / dodawanie
    # api/ticket            wyświetlanie ticketu przez użytkownika / dodawanie
]
