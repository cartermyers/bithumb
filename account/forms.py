from django import forms
from django.contrib.auth import password_validation

from . import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.User
        fields = ['username', 'password']

    def clean(self):
        #first, clean using the superclass
        cleaned_data = super(UserForm, self).clean()

        #make sure the password is valid:
        if not password_validation.validate_password(cleaned_data['password']):
            self.add_error('password', password_validation.password_validators_help_texts())
        else:
            if cleaned_data['password'] != cleaned_data['confirm_password']:
                self.add_error('confirm_password', "Passwords do not match.")

#there is no admin form because they should be registered by developers
