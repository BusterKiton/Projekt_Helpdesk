from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rights = models.CharField(
        max_length=10,
        choices=[('admin', 'Admin'), ('user', 'User')],
        default='user'
    )
    is_employee = models.BooleanField(default=False)  # Dodanie pola is_employee

    def __str__(self):
        return self.user.username
