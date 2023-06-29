from django import forms


class UserForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=99, )
    lastname = forms.CharField(min_length=1, max_length=99, )
    age = forms.IntegerField(min_value=1, max_value=99)