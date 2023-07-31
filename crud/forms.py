from django import forms
from crud.models import Student


class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'email']
