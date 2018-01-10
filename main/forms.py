from django import forms


class ParsePageForm(forms.Form):
    url = forms.URLField(label='Enter page link here', required=True)
