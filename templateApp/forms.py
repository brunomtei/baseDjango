from django import forms

class templateForm(forms.Form):
	name = forms.CharField(max_length=100)