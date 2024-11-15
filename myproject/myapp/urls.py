from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('panel_admina', views.panel_admina, name='panel_admina'),
    path('panel_usera', views.panel_usera, name='panel_usera'),
]