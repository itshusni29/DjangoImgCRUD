from django import forms
from .models import TrainingRequest
from profiles.models import Profiles
from django.contrib.auth.models import User

class TrainingRequestForm(forms.ModelForm):
    class Meta:
        model = TrainingRequest
        fields = ['title', 'participants', 'date', 'trainer', 'location', 'reason', 'manager', 'general_manager', 'attachments']

    def __init__(self, *args, **kwargs):
        super(TrainingRequestForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-control'
        
        self.fields['manager'].queryset = Profiles.objects.filter(Occupation='mng').select_related('user')
        self.fields['general_manager'].queryset = Profiles.objects.filter(Occupation='gm').select_related('user')
