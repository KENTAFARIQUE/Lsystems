from .models import SystemParameters
from django import forms

class GenerationForm(forms.Form):
    rules = forms.CharField()
    axiom = forms.CharField()
    iterations = forms.IntegerField()
    segment_length = forms.IntegerField()
    initial_heading = forms.IntegerField()
    angle_increment = forms.IntegerField()
    thickness = forms.IntegerField()
    color = forms.CharField()

class ImageParametersForm(forms.ModelForm):
    class Meta:
        model = SystemParameters
        fields = ['rules', 'axiom', 'iterations', 'segment_length', 'initial_heading', 'angle_increment', 'thickness', 'color']
        widgets = {
            'rules': forms.Textarea(attrs={'class': 'form-control'}),
            'axiom': forms.TextInput(attrs={'rows': 20, 'cols': 20}),
            'iterations': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'segment_length': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'initial_heading': forms.NumberInput(attrs={'min': 0, 'max': 360}),
            'angle_increment': forms.NumberInput(attrs={'min': 0, 'max': 360}),
            'thickness': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'color': forms.TextInput(attrs={'rows': 1, 'cols': 20})
        }




