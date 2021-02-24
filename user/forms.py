from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','email','username', 'password1', 'password2',)

    def clean(self):
        data = self.cleaned_data
        if "password1" in data and "password2" in data:
            if data["password1"] != data["password2"]:
                self._errors["password2"] = self.error_class(['Passwords do not match.'])
                del data['password2']
        return data
