from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "Must contain at least 8 characters, including both letters and numbers. Make it strong like a superhero!"

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Your secret agent email",
        widget=forms.TextInput(attrs={'placeholder': 'Your secret agent email'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']