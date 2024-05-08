from django import forms
from .models import Profiles

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['user', 'bio', 'Division', 'Department', 'Section', 'Occupation', 'profile_pic']
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
