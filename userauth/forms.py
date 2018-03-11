from django import forms

class LoginForm(forms.Form):
    UserName = forms.CharField(max_length=20)
    Password = forms.CharField(max_length=20, widget=forms.PasswordInput)