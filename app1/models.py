from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bewertung(models.Model):
    user = models.ForeignKey(User, verbose_name="Benutzer", on_delete=models.CASCADE)
    time = models.DateTimeField("Zeitpunkt", auto_now=False, auto_now_add=True)
    uebung = models.CharField("Uebung", max_length=50)
    ergebnis = models.IntegerField("Ergebnis")
    dauer = models.FloatField("Dauer", default=0)
    class Meta:
        verbose_name = "Bewertung"
        verbose_name_plural = "Bewertungen"

    def __str__(self):
        return f"{self.user} - {self.uebung} ({self.ergebnis}/{self.time}) "

    def get_absolute_url(self):
        return reverse("Bewertung_detail", kwargs={"pk": self.pk})
