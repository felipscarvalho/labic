from markdownx.fields import MarkdownxFormField
from django import forms
from .models import Articles


class Articles(forms.Form):
    markdownFile = MarkdownxFormField()

    model = Articles
    fields = '__all__'
