from django.db import models


class ProfileManager(models.Manager):
    def by_user(self, user):
        return self.filter(user=user)


class TicketManager(models.Manager):
    def by_requester(self, requester):
        return self.filter(requester=requester)

    def by_worker(self, worker):
        return self.filter(handler_worker=worker)
