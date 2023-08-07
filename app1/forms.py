from django import forms

class AnmeldeForm(forms.Form):
    buttons = (("Anmelden","success"),)
    name = forms.CharField(label="Anmeldename", max_length=50)
    password = forms.CharField(label="Passwort", max_length=50, widget=forms.PasswordInput)

class New_pwdForm(forms.Form):
    buttons = (("Passwort ändern","warning"),)
    pwd_old =  forms.CharField(label="altes Passwort", max_length=50, widget=forms.PasswordInput)
    pwd_new1 = forms.CharField(label="neues Passwort", max_length=50, widget=forms.PasswordInput)  
    pwd_new2 = forms.CharField(label="neues Passwort bestätigen", max_length=50, widget=forms.PasswordInput)  

class RegForm(forms.Form):
    buttons = (("Registrieren", "success"),)
    username = forms.CharField(label="Anmeldename", max_length=50)
    first_name = forms.CharField(label="Vorname", max_length=50)
    last_name = forms.CharField(label="Nachname", max_length=50)
    pwd_new1 = forms.CharField(label="neues Passwort", max_length=50, widget=forms.PasswordInput)  
    pwd_new2 = forms.CharField(label="neues Passwort bestätigen", max_length=50, widget=forms.PasswordInput)  
    ds_ok = forms.BooleanField(label="Ich bin einverstanden, dass hier meine Daten gespeichert und verarbeitet werden.")

class QuestForm(forms.Form):
    buttons = (("Abgeben", "success"),)
    aufgabe1 = forms.CharField(max_length=50 , required=False, widget=forms.TextInput(attrs={'readonly':'readonly'} ))
    zahl1 = forms.CharField(label="Ergebnis1", max_length=50)
    aufgabe2 = forms.CharField(max_length=50 , required=False, widget=forms.TextInput(attrs={'readonly':'readonly'} ))
    zahl2 = forms.CharField(label="Ergebnis2", max_length=50)
    aufgabe3 = forms.CharField(max_length=50 , required=False, widget=forms.TextInput(attrs={'readonly':'readonly'} ))
    zahl3 = forms.CharField(label="Ergebnis3", max_length=50)
    aufgabe4 = forms.CharField(max_length=50 , required=False, widget=forms.TextInput(attrs={'readonly':'readonly'} ))
    zahl4 = forms.CharField(label="Ergebnis5", max_length=50)
    aufgabe5 = forms.CharField(max_length=50 , required=False, widget=forms.TextInput(attrs={'readonly':'readonly'} ))
    zahl5 = forms.CharField(label="Ergebnis5", max_length=50)
