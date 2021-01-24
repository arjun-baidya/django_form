from django import forms
from django.core import validators


def check_validate(value):
    if len(value) < 6:
        raise forms.ValidationError("Password is too short it will be grater than six")


class SignUp(forms.Form):
    first_name = forms.CharField(initial='Arjun')
    last_name = forms.CharField(initial='Baidya')
    email = forms.EmailField(initial='abc@gmail.com')
    address = forms.CharField(required=False)
    technology = forms.CharField(initial='Django', disabled=True)
    age = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput, validators=[check_validate])
    re_password = forms.CharField(widget=forms.PasswordInput)

    # Validation
    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if len(password) < 4:
    #         raise forms.ValidationError("password is too short")
    #     return password
