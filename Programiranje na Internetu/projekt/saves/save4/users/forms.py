from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, views
from .models import CustomUser, Upisi

STATUS_CHOICES= [
    ('redovni', 'redovni'),
    ('izvanredni', 'izvanredni'),
]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=64)
    status = forms.CharField(max_length=10, widget=forms.Select(choices=STATUS_CHOICES))
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'status']

class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")

class UpdateUpisiForm(forms.Form):
    class Meta:
        model = Upisi