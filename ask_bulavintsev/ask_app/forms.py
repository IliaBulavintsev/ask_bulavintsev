from django import forms
from ask_app.models import *


class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class QuestionForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class AnswerForm(forms.Form):
    text = forms.CharField()
    quest = forms.CharField()