from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from pyuploadcare.dj.forms import ImageField

class RegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']






class ProfileForm(forms.ModelForm):
    profile_photo = ImageField(label='profile photo')

    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']


