from django import forms
from .models import Customer


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'date_of_birth', 'personal_number', 'gender']
