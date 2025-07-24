from django import forms
from .models import Incident
from .models import Comment

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'category', 'location', 'image', 'reporter_name']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']