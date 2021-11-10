from django import forms

class History(forms.Form):
    content = forms.CharField(required=True)