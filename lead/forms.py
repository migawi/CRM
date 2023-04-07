from django import forms

from .models import Lead, Comment

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'definition', 'priority', 'status')

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)