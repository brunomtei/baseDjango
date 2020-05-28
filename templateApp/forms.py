from django import forms

class templateForm(forms.Form):
	name = forms.CharField(max_length=100)

# Form Field Reference: https://docs.djangoproject.com/en/3.0/ref/forms/fields/

# forms.CharField(max_length=XXX, required=False|True, label='NNNN')
# forms.ModelChoiceField(queryset=XXXX.order_by('XXXX'), empty_label='NNNNN', required=False|True,label='NNNN')
# forms.ImageField()
# forms.BooleanField()

