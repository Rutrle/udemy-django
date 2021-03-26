from django import forms
from django.core import validators


def check_for_z(value):  # must take in value, best method if not in built-in validators
    if value[0].lower != 'z':
        raise forms.ValidationError("Needs to start with Z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify your email')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()  # return all cleaned data
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Your emails doesn't match")


"""
class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
                                 validators.MaxLengthValidator(0)])
    """

"""

    def clean_botcatcher(self):  # muse start with clean
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("Gotcha bot!")
"""
