from django import forms
from .models import Activity
from django.contrib.auth.models import User

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('title', 'description', 'type', 'start_time', 'end_time', 'published_date')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
