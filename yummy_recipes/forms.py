from django import forms
from django.forms import ModelForm
from .models import Comment, Recipe
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 4})

    class Meta:
        """
        Get the recipe model, choose fields to display and add summernote widget
        """
        model = Recipe
        fields = [
            'name',
            'description',
            'cook_time',
            'ingredients',
            'steps',
            'featured_image',
            'status',
        ]
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'steps': SummernoteWidget(),
        }
