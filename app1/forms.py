from django import forms

class AnmeldeForm(forms.Form):
    name = forms.CharField(label="Anmeldename", max_length=50)
    password = forms.CharField(label="Passwort", max_length=50, widget=forms.PasswordInput)

