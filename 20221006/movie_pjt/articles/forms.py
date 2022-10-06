from django.forms import ModelForm, TextInput, NumberInput
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'summary', 'running_time']
        widgets = {
            'title' : TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title',
            }),
            'summary': TextInput(attrs={
                'class':'form-control',
                'style':'height:500px;',
                'placeholder':'summary',
            }),
            'running_time':NumberInput(attrs={
                'class':'form-control',
            })
        }