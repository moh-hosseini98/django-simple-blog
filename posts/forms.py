from django import forms
from django.forms import ModelForm 
from .models import Comment





class CommentForm(forms.ModelForm):

    content =forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'type your comment',
        'id':'usercomment',
        'rows':'4'
    }))

    class Meta:
        model = Comment
        fields = ('content',)

