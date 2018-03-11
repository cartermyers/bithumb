from django import forms
from django.contrib.auth import password_validation

from . import models

class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Verify Password'}))

    class Meta:
        model = models.User
        fields = ['username', 'password']

    def clean(self):
        #first, clean using the superclass
        cleaned_data = super(SignupForm, self).clean()

        #make sure the password is valid:
        password = cleaned_data['password']
        confirm = cleaned_data['confirm_password']

        password_validation.validate_password(password)

        if password != confirm:
            self.add_error('confirm_password', "Passwords do not match.")

#there is no admin form because they should be registered by developers

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    keep_me_logged_in = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id': 'show_label'}))
