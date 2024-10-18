from django import forms

from Fruitipedia_App.fruit.models import Fruit


class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = [
            'name', 'image_url', 'description',
            'nutrition'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Fruit Name',
                'class': 'form-control'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Fruit Image URL',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Fruit Description',
                'class': 'form-control',
            }),
            'nutrition': forms.Textarea(attrs={
                'placeholder': 'Nutrition Info',
                'class': 'form-control',
            }),
        }
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Fruit Name',
                'class': 'form-control'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Fruit Image URL',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Fruit Description',
                'class': 'form-control',
            }),
            'nutrition': forms.Textarea(attrs={
                'placeholder': 'Nutrition Info',
                'class': 'form-control',
            }),
        }


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'















