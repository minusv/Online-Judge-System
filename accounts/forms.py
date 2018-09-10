from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username',
            widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter username"}))
    email = forms.EmailField(label='Email',
            widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Email address"}))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Enter Password",}))
    password2 = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Confirm your Password",}))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        check_username = User.objects.filter(username=username)
        if check_username.exists():
            raise forms.ValidationError("Username taken")
        return username
    
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password!=password2:
            raise forms.ValidationError("Password must match")
        return data

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',
            widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter username"}))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Enter Password",}))
    