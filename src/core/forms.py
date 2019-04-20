from django import forms
from django.contrib.postgres.fields import IntegerRangeField, DateRangeField
from .models import Category


class FilterForm(forms.Form):
    title = forms.CharField()
    id_exact = forms.IntegerField(min_value=0)
    title_or_author = forms.CharField()
    views_range = IntegerRangeField()
    date_range = DateRangeField()
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all())
    reviewed = forms.ChoiceField(widget=forms.ChoiceWidget
