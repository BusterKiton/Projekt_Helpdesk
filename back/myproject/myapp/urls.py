from django.urls import path, include
from . import views
from .views import HelloWorld, RegisterView, LoginAPIView,UserTicketsApiView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('panel_admina/', views.panel_admina, name='panel_admina'),
    path('panel_usera/', views.panel_usera, name='panel_usera'),
    path('api/hello/', HelloWorld.as_view(), name='hello-world'),
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/login/', LoginAPIView.as_view(), name='api-login'),
    path('api/user/', UserTicketsApiView.as_view(), name='api-user'),

]
