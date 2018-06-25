from django import forms

class AddUser(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    salary = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
