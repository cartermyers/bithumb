from django import forms

from . import models

class ForumForm(forms.ModelForm):
    # may be needed for later
    #title = forms.CharField(widget=forms.CharField(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    #description = forms.CharField(widget=forms.CharField(attrs={'class': 'form-control', 'placeholder': 'Verify Password'}))

    class Meta:
        model = models.Forum
        fields = ['title', 'description']