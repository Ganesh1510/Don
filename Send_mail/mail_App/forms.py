from django import forms

class EmailForm(forms.Form):
    to_email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
