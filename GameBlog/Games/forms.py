from django import forms
from .models import Category, Games
import re
from django.core.exceptions import ValidationError

class GamesForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValueError('Заголовок не должен начинаться с цифр')
        return title

    class Meta:
        model = Games
    #fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
        'title': forms.TextInput(attrs={
            'class': 'form-control'
        }),
        'content': forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5
        }),
        'category': forms.Select(attrs={
            'class': 'form-control'
    }),
    }
    # title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={
    #     'class': 'form-control'
    # }))
    # content = forms.CharField(label='Описание', required=False, widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'rows': 5
    # }))
    # is_published = forms.BooleanField(label='Публикация', initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Жанр', empty_label='Выберите жанр', widget=forms.Select(attrs={
    #     'class': 'form-control'
    # }))