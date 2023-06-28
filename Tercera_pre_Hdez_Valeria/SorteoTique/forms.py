from django import forms

class formRegisterClient(forms.Form):
    client_id = forms.CharField(max_length=30)
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()