# forms.py
from django import forms
from .models import contact1

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact1
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Your Email'}),
            'mobileno':forms.NumberInput(attrs={'placeholder':'Mobile No'}),
            'message':forms.Textarea(attrs={'placeholder':'Enter Your Message','cols':'60'}),
        }