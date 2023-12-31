# Generated by Django 4.2.3 on 2023-08-07 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bewertung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Zeitpunkt')),
                ('uebung', models.CharField(max_length=50, verbose_name='Uebung')),
                ('ergebnis', models.IntegerField(verbose_name='Ergebnis')),
                ('dauer', models.FloatField(default=0, verbose_name='Dauer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Benutzer')),
            ],
            options={
                'verbose_name': 'Bewertung',
                'verbose_name_plural': 'Bewertungs',
            },
        ),
    ]
