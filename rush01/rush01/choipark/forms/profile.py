from django import forms
from ..models import UserProfileModel


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['description'].required = False
        self.fields['profile_image'].required = False
        self.fields['surname'].required = False
        self.fields['name'].required = False

    class Meta:
        model = UserProfileModel
        fields = ['name', 'surname', 'email', 'description', 'profile_image']
