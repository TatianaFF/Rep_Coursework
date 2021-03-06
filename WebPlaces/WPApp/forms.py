from django import forms
from django.contrib.auth.models import User

from .models import Place, Favorite, Comment


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
