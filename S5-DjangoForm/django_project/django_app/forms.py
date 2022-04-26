from django import forms
from django.core import validators
from django_app.models import User


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('NAME NEED TO START WITH Z')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(
        label='', widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']

        if len(botcatcher) > 0:
            raise forms.ValidationError('GOTCHA BOT!')

        return botcatcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError('EMAIL DOESN\'T MATCH!')


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     print(password)

    #     if len(password) < 8:
    #         raise forms.ValidationError('Password must at least 8 characters!')

    #     return password
