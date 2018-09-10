from django import forms
from .models import question

class question_form(forms.ModelForm):
    quescode = forms.CharField(label='Question Code:',
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Eg. AVGPR"}))
    timelimit = forms.CharField(label='Timelimit:',
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "0.00"}))
    ip_file = forms.FileField(label='Input File:',
        widget=forms.ClearableFileInput(attrs={"class":"form-control-file"}))
    op_file = forms.FileField(label='Output File:',
        widget=forms.ClearableFileInput(attrs={"class":"form-control-file"}))

    class Meta:
        model = question
        fields = ('quescode', 'timelimit','ip_file','op_file')
    
    def clean_quescode(self):
        quescode = self.cleaned_data.get('quescode')
        check_quescode = question.objects.filter(quescode=quescode)
        if check_quescode.exists():
            raise forms.ValidationError("Question already exists.")
        return quescode
    
class edit_question_form(forms.ModelForm):
    timelimit = forms.CharField(label='Timelimit:',
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "0.00"}))
    ip_file = forms.FileField(label='Input File:',
        widget=forms.ClearableFileInput(attrs={"class":"form-control-file"}))
    op_file = forms.FileField(label='Output File:',
        widget=forms.ClearableFileInput(attrs={"class":"form-control-file"}))

    class Meta:
        model = question
        fields = ('timelimit','ip_file','op_file')