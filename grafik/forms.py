# forms.py
from django import forms
from .models import ChartData

class ChartDataForm(forms.ModelForm):
    class Meta:
        model = ChartData
        fields = ['month', 'actual_value', 'target_value']
