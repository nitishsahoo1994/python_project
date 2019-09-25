from django import forms

class EmailSendForm(forms.Form):
    name=forms.CharField()
    mail=forms.EmailField()
    to=forms.EmailField()
    # comments=forms.CharField(forms.Textarea())


#create comment Form
from testapp.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','comment']

