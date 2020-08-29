from django import forms

class AddPerson(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    salary = forms.IntegerField()
    country = forms.CharField()
    city = forms.CharField()
