from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rights = models.CharField(
        max_length=10,
        choices=[('admin', 'Admin'), ('user', 'User'), ('worker', 'Worker')],
        default='user'
    )
    is_employee = models.BooleanField(default=False)  # Dodanie pola is_employee

    def __str__(self):
        return self.user.username


# Do zrobienia
# Dodać kategorie
# dodać Chat
# dodać obsługe plików
class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    requester = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="requested_tickets")
    handler_worker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="handled_tickets")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.requester.user.username} - {self.handler_worker.user.username}"


class Status(models.Model):
    name = models.CharField(
        choices=[('new', 'New'),
                 ('in_prog', 'In Progress '),
                 ('rejected', 'Rejected'),
                 ('resolved', 'Resolved'),
                 ('reopened', 'Reopened'),
                 ('closed', 'Closed')
                 ],
        default='user'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    replaced_at = models.DateTimeField(null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="statuses")

    def __str__(self):
        return f"{self.name} - {self.ticket.title}"
