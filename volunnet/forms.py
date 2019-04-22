from django import forms
from .models import Activity, Organization, Volunteer
from django.contrib.auth.models import User


#added by CV
from django.db import models
import django_filters


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('title', 'description', 'type', 'start_time', 'end_time', 'published_date')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Re-enter password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class OrganizationRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Re-enter password', widget=forms.PasswordInput)

    class Meta:
        model = Organization
        fields = ('name', 'address', 'state','city', 'zipcode', 'email', 'phone')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#added by amber
class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('title','vol_name', 'email', 'phone_number','vol_date', 'start_time', 'end_time','applied_time' )

#added by CV
class ActiivtyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    type = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)

    class Meta:
        model = Activity
        fields = ['title', 'description', 'type']
