from django import forms
from Fruitipedia_App.user.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name', 'last_name',
            'email', 'password'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control',
            }),
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name', 'last_name',
            'image_url', 'age'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name',
                'class': 'form-control'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Enter your profile image URL',
                'class': 'form-control'
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter your age',
                'class': 'form-control'
            }),
        }


class DeleteUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()























