from django import forms
from judge.models import question
from .models import status

class Submit_Program(forms.ModelForm):
        CHOICE=(('1', 'Python'),)
        quesid= forms.ModelChoiceField(queryset = question.objects.all(),label='Select Question',
                widget=forms.Select(attrs={'class':'form-control'}))
        language = forms.ChoiceField(required=False,choices=CHOICE,label='Select Language',
                widget=forms.Select(attrs={'class':'form-control'}))
        source_code = forms.FileField(label='Input File:',
            widget=forms.ClearableFileInput(attrs={"class":"form-control-file"}))
        
        class Meta:
                model = status
                fields = ('quesid','language','source_code')
        