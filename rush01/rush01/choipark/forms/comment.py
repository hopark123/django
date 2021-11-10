from django import forms
from ..models import CommentsModel, ReplyModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ["comment",]


class ReplyForm(forms.ModelForm):
    class Meta:
        model = ReplyModel
        fields = ["reply",]
