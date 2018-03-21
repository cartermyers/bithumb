from django import forms

from . import models

class ForumForm(forms.ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'type': 'title', 'id': 'title', 'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'id': 'desc'}), required=False)

    class Meta:
        model = models.Forum
        fields = ['title', 'description']

class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=500, widget=forms.TextInput({'class': "form-control", 'name': "comments", 'id': "comments",  'placeholder': "comments"}))

    class Meta:
        model = models.Comments
        fields = ['text']
