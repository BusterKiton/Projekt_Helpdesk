from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Profile, FileAttachment, Ticket
from .serializers import FileAttachmentSerializer, TicketSerializer
from django.core.cache import cache
import redis

# API Endpoint do przesyłania plików
class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, ticket_id, *args, **kwargs):
        try:
            # Pobierz zgłoszenie
            ticket = Ticket.objects.get(id=ticket_id)

            # Pobierz plik
            file = request.FILES['file']

            # Walidacja rozmiaru pliku
            if file.size > 10 * 1024 * 1024:  # 10 MB limit
                return Response({"error": "File too large"}, status=400)

            # Tworzenie załącznika
            attachment = FileAttachment.objects.create(
                ticket=ticket,
                uploaded_by=request.user,
                file=file
            )
            return Response(FileAttachmentSerializer(attachment).data, status=201)
        except Ticket.DoesNotExist:
            return Response({"error": "Ticket not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


# API Endpoint do listy zgłoszeń
class TicketListView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

# Widoki HTML
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
                # Tworzenie użytkownika
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # Tworzenie profilu użytkownika
                Profile.objects.create(user=user, user_rights=user_rights)

                messages.success(request, 'Rejestracja zakończona sukcesem!')
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
