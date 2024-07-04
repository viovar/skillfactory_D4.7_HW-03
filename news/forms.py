from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'rating',
            'postCategory',
            'author'
        ]

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('title')
            description = cleaned_data.get('text')
            if name == description:
                raise ValidationError(
            "Описание не должно быть идентично названию"
                )
            return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'postCategory']

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('title')
            description = cleaned_data.get('text')
            if name == description:
                raise ValidationError(
            "Описание не должно быть идентично названию"
                )
            return cleaned_data