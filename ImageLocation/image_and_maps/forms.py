from django import forms
from django.forms import widgets
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('name', 'description', 'image')

        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'image': widgets.FileInput(attrs={'class': 'form-control'}),
        }
