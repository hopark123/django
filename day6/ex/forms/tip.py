from django import forms
from ..models import TipModel

class TipForm(forms.Form):
    content = forms.CharField(required=True)