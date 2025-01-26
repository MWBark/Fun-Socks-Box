from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """
    Form class for sending contact message.
    """
    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'message')
