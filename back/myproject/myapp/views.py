from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login as auth_login
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
import logging
User = get_user_model()

logger = logging.getLogger(__name__)
class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello from Django!"})
# Create your views here.
def index(request):
    return render(request, 'index.html')
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        is_employee = request.data.get('is_employee', False)

        # Walidacja pustych pól
        if not username or not email or not password:
            return Response({"message": "Wszystkie pola są wymagane."}, status=status.HTTP_400_BAD_REQUEST)

        # Sprawdzenie, czy użytkownik już istnieje
        if User.objects.filter(username=username).exists():
            return Response({"message": "Użytkownik o podanej nazwie już istnieje."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"message": "Użytkownik z podanym adresem e-mail już istnieje."}, status=status.HTTP_400_BAD_REQUEST)

        # Tworzenie użytkownika
        user = User.objects.create_user(username=username, email=email, password=password)
        if hasattr(user, 'profile'):  # Jeśli istnieje model Profile
            user.profile.is_employee = is_employee
            user.profile.save()

        return Response({"message": "Rejestracja zakończona sukcesem."}, status=status.HTTP_201_CREATED)

User = get_user_model()
logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name='dispatch')


@method_decorator(csrf_exempt, name='dispatch')
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"message": "Wszystkie pola są wymagane."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"message": "Logowanie zakończone sukcesem.", "token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Nieprawidłowe dane logowania."}, status=status.HTTP_401_UNAUTHORIZED)
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        user_rights = request.POST.get('user_rights', 'user')  # Domyślnie 'user'

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email już istnieje')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Nazwa użytkownika jest zajęta')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # Ustaw prawa użytkownika
                profile = Profile.objects.get(user=user)
                profile.user_rights = user_rights
                profile.save()

                return redirect('login')
        else:
            messages.info(request, 'Hasła nie są te same')
            return redirect('register')
    else:
        return render(request, 'register.html')
def panel_admina(request):
    return render(request, 'panel_admina.html')
def panel_usera(request):
    return render(request, 'panel_usera.html')
User = get_user_model()

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Wszystkie pola są wymagane.')
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            if hasattr(user, 'profile') and user.profile.user_rights == 'admin':
                return redirect('panel_admina')
            else:
                return redirect('panel_usera')
        else:
            messages.error(request, 'Nieprawidłowe dane logowania.')
            return redirect('login')

    return render(request, 'login.html')