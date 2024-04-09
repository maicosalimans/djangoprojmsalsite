from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.management.base import BaseCommand


class Voetbalspelers(models.Model):
    naam_auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    naam_voetballer = models.CharField(max_length=200)
    actuele_club = models.CharField(max_length=200)
    datum_invoer = models.DateTimeField(default=timezone.now)
    datum_laatste_aanpassing = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.naam_voetballer


