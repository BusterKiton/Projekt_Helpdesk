from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
# Create your views here.
def index(request):
    return render(request, 'index.html')

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
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            # Pobierz prawa użytkownika
            user_rights = user.profile.user_rights
            if user_rights == 'admin':
                return redirect('panel_admina')
            elif user_rights == 'user':
                return redirect('panel_usera')
        else:
            messages.info(request, 'Nieprawidłowe dane logowania')
            return redirect('login')
    else:
        return render(request, 'login.html')
