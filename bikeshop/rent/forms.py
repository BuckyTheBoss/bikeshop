from django import forms
from .models import Address

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=20) 
    last_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=25)
    address = forms.ModelChoiceField(queryset=Address.objects.all())
