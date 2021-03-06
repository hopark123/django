from django import forms

class UpdateForm(forms.Form):
    title = forms.ChoiceField(choices=(), required=True)

    def __init__(self, choices, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].choices = choices