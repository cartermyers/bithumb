from django import forms

from . import models

class ForumForm(forms.ModelForm):
    # may be needed for later
    #title = forms.CharField(widget=forms.CharField(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    description = forms.CharField(widget=forms.Textarea(), required=False)

    class Meta:
        model = models.Forum
        fields = ['title', 'description']

class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comments
        fields = ['text']
