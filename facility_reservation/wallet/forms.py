from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfileInfo

User = get_user_model()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfileInfo
        fields = ('first_name', 'last_name', 'confirm_password')
        widgets = {
            'password': forms.PasswordInput(),
        }
