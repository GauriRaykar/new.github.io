from django import forms
from .models import Submission

class SubmissionForm(forms.Form):
    email = forms.CharField()