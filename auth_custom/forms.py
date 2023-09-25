from django import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=120)
    password = forms.CharField(
        widget=forms.PasswordInput,
        max_length=120
    )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(
        widget=forms.PasswordInput,
        max_length=120
    ) 