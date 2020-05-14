from django import forms
from .models import Korisnici


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = Korisnici
        fields = ['email', 'password1', 'password2']