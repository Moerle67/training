from django import forms

class AnmeldeForm(forms.Form):
    buttons = (("Anmelden","success"),)
    name = forms.CharField(label="Anmeldename", max_length=50)
    password = forms.CharField(label="Passwort", max_length=50, widget=forms.PasswordInput)

class New_pwdForm(forms.Form):
    buttons = (("Passwort ändern","warning"),)
    pwd_old =  forms.CharField(label="altes Passwort", max_length=50, widget=forms.PasswordInput)
    pwd_new1 = forms.CharField(label="neues Passwort", max_length=50, widget=forms.PasswordInput)  
    pwd_new2 = forms.CharField(label="neues Passwort2", max_length=50, widget=forms.PasswordInput)  

