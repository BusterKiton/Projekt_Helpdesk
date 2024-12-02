from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .managers import ProfileManager

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rights = models.CharField(
        max_length=10,
        choices=[('admin', 'Admin'), ('user', 'User'), ('worker', 'Worker')],
        default='user'
    )
    is_employee = models.BooleanField(default=False)  # Dodanie pola is_employee
    objects = ProfileManager()

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
    handler_worker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="handled_tickets", null=True,
                                       blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


# NIE DZIAŁA
    def get_handler_worker_if_exist(self):
        if self.handler_worker:
            return self.handler_worker.user.username
        else:
            return "NONE"

    def validateHandlerPermissions(self):
        if self.handler_worker.user_rights == "admin" or self.handler_worker.user_rights == "worker":
            return True
        else:
            raise ValidationError("Podana osoba nie jest pracownikiem")

    def validateHandlerRequester(self):
        if self.requester.id == self.handler_worker.id:
            raise ValidationError("Pracownik rozwiązuje własny problem!")
        else:
            return True

    def clean(self):
        super().clean()
        try:
            self.validateHandlerPermissions()
            self.validateHandlerRequester()
        except ValidationError as ex:
            raise ValidationError(ex.message)
        print("TEST")

    def __str__(self):
        return f"{self.title} - {self.requester.user.username} - {self.get_handler_worker_if_exist()}"


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
    replaced_at = models.DateTimeField(null=True, blank=True)  # Dodać funkcje uzupełniającą
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="statuses")

    def __str__(self):
        return f"{self.name} - {self.ticket.title}"
