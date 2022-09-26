from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',) ## burda diyoruz ki, user field kullanma, digerlerini kullan.
        # fields = ('bio', 'profile_pic', 'user') 

class UserUpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')