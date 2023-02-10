from django import forms
from .models import Post

class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title_news',
            'text_news',
            ]

    def clean(self):
        cleaned_data = super().clean()
        text_news = cleaned_data.get("text_news")
        title_news = cleaned_data.get("title_news")
        if title_news == text_news:
            raise ValidationError(
                "Новость не должно быть идентично названию новости."
            )
        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title_news',
            'text_news',
            ]

    def clean(self):
        cleaned_data = super().clean()
        text_news = cleaned_data.get("text_news")
        title_news = cleaned_data.get("title_news")
        if title_news == text_news:
            raise ValidationError(
                "Новость не должно быть идентично названию новости."
            )
        return cleaned_data

class NewsDeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title_news',
            'text_news',
            ]

class ArticleDeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title_news',
            'text_news',
            ]