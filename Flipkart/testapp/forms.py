from django import forms
from django.contrib.auth.models import User
from .models import CartItem

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        password = cleaned_data['password']
        confirm_password = cleaned_data['re_password']
        if password!=confirm_password:
            raise forms.ValidationError("Password Not Matched")
        
class CartUpdate(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)