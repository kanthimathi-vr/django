from django import forms
from .models import Contact
import re

# Manual Form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if re.search(r'\d', name):
            raise forms.ValidationError("Name must not contain numbers")
        return name


# ModelForm
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if re.search(r'\d', name):
            raise forms.ValidationError("Name must not contain numbers")
        return name
