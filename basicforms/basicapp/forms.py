from django import forms
from django.core import validators

class formName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verfy_email = forms.EmailField(label='Enter your email again')
    text  = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email :
            raise forms.ValidationError("MAKE SURE EMAIL MATCH!")
