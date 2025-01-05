from rest_framework import serializers
from .models import Ticket, Profile

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'  # Serializuje wszystkie pola modelu

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'user_rights', 'is_employee']  # Wybierz pola, które chcesz serializować
