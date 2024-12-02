from django.db import models


class ProfileManager(models.Manager):
    def by_user(self, user):
        return self.filter(user=user)
