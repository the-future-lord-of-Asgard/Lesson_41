from django import forms
from .models import Advertisements81
from django.core.exceptions import ValidationError

class Advertisement81Form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'
        self.fields['bu'].widget.attrs['class'] = 'form-check-input'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        model = Advertisements81
        fields = ('title', 'description', 'price', 'auction', 'bu', 'image')

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startwith('?'):
            raise ValidationError('НЕЛЬЗЯ! Нельзя! Нельзя начинать заголовок с вопросительного знака!')
        return title
